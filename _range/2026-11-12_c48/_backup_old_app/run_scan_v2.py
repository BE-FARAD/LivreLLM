import os
import shutil
import json
import time
import uuid
import re
import math
from dotenv import load_dotenv
from pypdf import PdfReader, PdfWriter
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.http import models
from fastembed import TextEmbedding
from core.scanner import scan_pdf_with_marker, cleanup_failed_scan

# Load environment variables
load_dotenv()

# Directories
INPUTS_DIR = "01_INPUTS"
LIBRARY_DIR = "library_data"
if not os.path.exists(INPUTS_DIR): os.makedirs(INPUTS_DIR, exist_ok=True)
if not os.path.exists(LIBRARY_DIR): os.makedirs(LIBRARY_DIR, exist_ok=True)

# OpenAI
try:
    client_openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except:
    client_openai = None

def split_pdf(input_path, output_dir, chunk_size=25):
    """Split PDF into chunks of pages."""
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)
    chunks = []
    
    print(f"Splitting PDF ({total_pages} pages) into chunks of {chunk_size}...")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for i in range(0, total_pages, chunk_size):
        writer = PdfWriter()
        end_page = min(i + chunk_size, total_pages)
        
        for page_num in range(i, end_page):
            writer.add_page(reader.pages[page_num])
            
        chunk_filename = f"chunk_{i:04d}_{end_page:04d}.pdf"
        chunk_path = os.path.join(output_dir, chunk_filename)
        
        with open(chunk_path, "wb") as f:
            writer.write(f)
            
        chunks.append(chunk_path)
        
    return chunks

def merge_markdowns(chunk_results):
    """Merge multiple markdown contents into one."""
    full_text = ""
    for path in sorted(chunk_results):
        if not os.path.exists(path): continue
        with open(path, "r") as f:
            full_text += f.read() + "\n\n"
    return full_text

def process_new_files_segmented():
    # Force CPU for stability
    os.environ["TORCH_DEVICE"] = "cpu" 
    os.environ["OCR_DEVICE"] = "cpu"
    os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
    
    pdf_files = [f for f in os.listdir(INPUTS_DIR) if f.endswith(".pdf")]
    if not pdf_files:
        print("No PDF files found.")
        return

    for pdf_file in pdf_files:
        print(f"=== Processing: {pdf_file} ===")
        book_id = re.sub(r'[^\w\-_\.]', '', pdf_file.replace(".pdf", "").replace(" ", "_"))
        book_dir = os.path.join(LIBRARY_DIR, book_id)
        
        if not os.path.exists(book_dir): os.makedirs(book_dir)
        
        # 1. SPLIT PDF
        temp_split_dir = os.path.join(book_dir, "_temp_splits")
        input_pdf_path = os.path.join(INPUTS_DIR, pdf_file)
        
        try:
            chunks = split_pdf(input_pdf_path, temp_split_dir, chunk_size=20) # 20 pages per batch is safe
            
            chunk_md_files = []
            
            # 2. PROCESS CHUNKS SEQUENTIALLY
            for i, chunk_path in enumerate(chunks):
                print(f"--> Processing Batch {i+1}/{len(chunks)}...")
                try:
                    # Create a specific output dir for this chunk to avoid marker collisions
                    chunk_out_dir = os.path.join(temp_split_dir, f"out_{i}")
                    md_file = scan_pdf_with_marker(chunk_path, chunk_out_dir)
                    chunk_md_files.append(md_file)
                    
                    # Copy images immediately to main book dir
                    source_images_dir = os.path.dirname(md_file)
                    if os.path.basename(source_images_dir) != os.path.basename(book_dir):
                        for item in os.listdir(source_images_dir):
                            if item.endswith(".png") or item.endswith(".jpg"):
                                s = os.path.join(source_images_dir, item)
                                d = os.path.join(book_dir, item)
                                if not os.path.exists(d): shutil.copy2(s, d)
                                
                except Exception as e:
                    print(f"FAILED Batch {i+1}: {e}")
                    # Continue gracefully? Yes, missing 20 pages is better than failing all
            
            # 3. MERGE
            print("Merging results...")
            full_md = merge_markdowns(chunk_md_files)
            
            final_md_path = os.path.join(book_dir, "content.md")
            with open(final_md_path, "w") as f:
                f.write(full_md)
                
            # Cleanup temp
            shutil.rmtree(temp_split_dir)
            
            # 4. STRUCTURE & METADATA
            # Simple structure based on headers
            chapter_splits = re.split(r'(^# .+)', full_md, flags=re.MULTILINE)
            chapters = []
            if len(chapter_splits) > 1:
                if chapter_splits[0].strip(): chapters.append(chapter_splits[0])
                for i in range(1, len(chapter_splits), 2):
                    title = chapter_splits[i].strip()
                    content = chapter_splits[i+1] if i+1 < len(chapter_splits) else ""
                    chapters.append(title + "\n" + content)
            else:
                chapters = [full_md]
                
            # Save chapters
            for i, content in enumerate(chapters):
                with open(os.path.join(book_dir, f"chapter_{i+1}.txt"), "w") as f:
                    f.write(content)
                    
            # Metadata
            metadata = {
                "id": book_id,
                "title": pdf_file.replace(".pdf", ""),
                "author": "Unknown",
                "summary": "Processed via Batched Scan",
                "total_chapters": len(chapters),
                "processed_at": time.time()
            }
            with open(os.path.join(book_dir, "metadata.json"), "w") as f:
                json.dump(metadata, f, indent=4)

            # Move processed file
            processed_dir = os.path.join(INPUTS_DIR, "processed")
            if not os.path.exists(processed_dir): os.makedirs(processed_dir)
            shutil.move(input_pdf_path, os.path.join(processed_dir, pdf_file))
            
            print(f"SUCCESS! Book processed in {len(chunks)} batches.")
            
        except Exception as e:
            print(f"CRITICAL ERROR: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    process_new_files_segmented()
