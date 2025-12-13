import os
import shutil
import json
import time
import uuid
import re
from dotenv import load_dotenv
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.http import models
from fastembed import TextEmbedding
from core.scanner import scan_pdf_with_marker

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
except Exception as e:
    print(f"Warning: OpenAI client init failed: {e}")
    client_openai = None

# Qdrant
print("Initializing Vector DB...")
try:
    client_qdrant = QdrantClient(path="local_qdrant_db")
    embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
    
    COLLECTION_NAME = "books_collection"
    VECTOR_SIZE = 384
    
    try:
        collections = client_qdrant.get_collections().collections
        exists = any(c.name == COLLECTION_NAME for c in collections)
        if not exists:
            client_qdrant.create_collection(collection_name=COLLECTION_NAME, vectors_config=models.VectorParams(size=VECTOR_SIZE, distance=models.Distance.COSINE))
    except:
        pass
except Exception as e:
    print(f"Error initializing DB: {e}")
    client_qdrant = None

def save_book_metadata(book_id, metadata):
    path = os.path.join(LIBRARY_DIR, book_id, "metadata.json")
    with open(path, "w") as f: json.dump(metadata, f, indent=4)

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += (chunk_size - overlap)
    return chunks

def index_document(text, filename):
    if not client_qdrant: return
    chunks = chunk_text(text)
    points = []
    print(f"Embedding {len(chunks)} chunks...")
    embeddings = list(embedding_model.embed(chunks))
    
    for i, (chunk, vector) in enumerate(zip(chunks, embeddings)):
        points.append(models.PointStruct(
            id=str(uuid.uuid4()),
            vector=vector.tolist(),
            payload={"text": chunk, "filename": filename}
        ))
    
    client_qdrant.upsert(collection_name=COLLECTION_NAME, points=points)
    print("Indexing complete.")

def process_new_files_cli():
    pdf_files = [f for f in os.listdir(INPUTS_DIR) if f.endswith(".pdf")]
    
    if not pdf_files:
        print("No new PDF files found in 01_INPUTS.")
        return

    for pdf_file in pdf_files:
        print(f"Found file: {pdf_file}")
        book_id = pdf_file.replace(".pdf", "").replace(" ", "_").replace("__", "_")
        # Sanitize book_id further if needed to be safe path
        book_id = re.sub(r'[^\w\-_\.]', '', book_id)
        
        book_dir = os.path.join(LIBRARY_DIR, book_id)
        
        if not os.path.exists(book_dir):
            os.makedirs(book_dir)
            print(f"Created directory: {book_dir}")
            
            # FORCE CPU FOR STABILITY (Mac MPS issues workaround)
            os.environ["TORCH_DEVICE"] = "cpu" 
            os.environ["OCR_DEVICE"] = "cpu"
            print("Forcing CPU mode for stability...")
            
            # 1. SCAN
            print(f"Scanning {pdf_file} with Marker...")
            try:
                input_pdf_path = os.path.join(INPUTS_DIR, pdf_file)
                md_path = scan_pdf_with_marker(input_pdf_path, book_dir)
                
                # 2. Post-process (Move MD)
                final_md_path = os.path.join(book_dir, "content.md")
                if md_path != final_md_path:
                    shutil.copy2(md_path, final_md_path)
                    # Copy images
                    source_images_dir = os.path.dirname(md_path)
                    if os.path.basename(source_images_dir) != os.path.basename(book_dir):
                        for item in os.listdir(source_images_dir):
                            s = os.path.join(source_images_dir, item)
                            d = os.path.join(book_dir, item)
                            if os.path.exists(d):
                                if os.path.isdir(d): shutil.rmtree(d)
                                else: os.remove(d)
                            if os.path.isdir(s): shutil.copytree(s, d)
                            else: shutil.copy2(s, d)

                # 3. Read content
                with open(final_md_path, "r") as f:
                    md_text = f.read()
                
                print("Conversion successful. Processing structure...")

                # 4. Split Chapters
                chapter_splits = re.split(r'(^# .+)', md_text, flags=re.MULTILINE)
                chapters = []
                if len(chapter_splits) > 1:
                    if chapter_splits[0].strip():
                        chapters.append({"title": "Introduction", "content": chapter_splits[0]})
                    for i in range(1, len(chapter_splits), 2):
                        title = chapter_splits[i].strip().replace("#", "").strip()
                        content = chapter_splits[i+1] if i+1 < len(chapter_splits) else ""
                        chapters.append({"title": title, "content": title + "\n\n" + content})
                else:
                    chapters = [{"title": "Livre entier", "content": md_text}]
                
                # 5. Save Chapters & Translate
                print(f"Found {len(chapters)} chapters/sections.")
                
                for i, chap in enumerate(chapters):
                    # Save EN
                    with open(os.path.join(book_dir, f"chapter_{i+1}.txt"), "w") as f:
                        f.write(chap['content'])
                    
                    # Translate
                    print(f"Translating chapter {i+1}...")
                    if client_openai:
                        try:
                            clean_prompt = f"""
                            Tu es un expert technique et traducteur.
                            TA TÂCHE : Traduire et Formater ce contenu technique en FRANÇAIS.
                            
                            CONSIGNES STRICTES DE FORMATAGE :
                            1. **MATHÉMATIQUES** : Repère les formules et réécris-les proprement en LaTeX (entre $$ pour les blocs, $ pour le texte).
                            2. **CODE** : Repère les blocs de code et entoure-les de triples backticks (```python, etc.). NE TRADUIS PAS LE CODE, traduis seulement les commentaires.
                            3. **STRUCTURE** : Garde les titres Markdown (#, ##).
                            4. **TEXTE** : Traduis les explications en français fluide.
                            
                            TEXTE BRUT À TRAITER :
                            {chap['content'][:15000]} 
                            """
                            response = client_openai.chat.completions.create(
                                model="gpt-4o", messages=[{"role": "system", "content": clean_prompt}]
                            )
                            fr_content = response.choices[0].message.content
                        except Exception as e:
                            print(f"Translation error: {e}")
                            fr_content = chap['content'] # Fallback
                    else:
                        fr_content = chap['content']

                    with open(os.path.join(book_dir, f"chapter_{i+1}_fr.txt"), "w") as f:
                        f.write(fr_content)
                
                # 6. Indexing
                print("Indexing for RAG...")
                try:
                    index_document(md_text, pdf_file)
                except Exception as e:
                    print(f"RAG Indexing Warning: {e}")
                
                # Summary
                print("Generating summary...")
                summary = "Résumé non disponible."
                if client_openai:
                    try:
                        summary_prompt = f"Fais un résumé court et accrocheur (2 phrases) en FRANÇAIS de ce livre : {chapters[0]['content'][:2000]}..."
                        summary = client_openai.chat.completions.create(
                           model="gpt-4o", messages=[{"role": "system", "content": summary_prompt}]
                        ).choices[0].message.content
                    except: pass
                
                # Metadata
                metadata = {
                    "id": book_id,
                    "title": pdf_file.replace(".pdf", "").replace("_", " "),
                    "author": "Inconnu",
                    "summary": summary,
                    "total_chapters": len(chapters),
                    "processed_at": time.time()
                }
                save_book_metadata(book_id, metadata)
                
                # Move PDF
                processed_dir = os.path.join(INPUTS_DIR, "processed")
                if not os.path.exists(processed_dir): os.makedirs(processed_dir)
                shutil.move(input_pdf_path, os.path.join(processed_dir, pdf_file))
                
                print(f"Book '{metadata['title']}' added successfully!")

            except Exception as e:
                print(f"Error processing {pdf_file}: {e}")
                import traceback
                traceback.print_exc()

if __name__ == "__main__":
    process_new_files_cli()
