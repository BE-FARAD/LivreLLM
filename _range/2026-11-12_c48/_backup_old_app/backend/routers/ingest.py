from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from backend.services.ingestion_service import IngestionService
from backend.services.vector_service import VectorService
from backend.services.graph_service import GraphService
from backend.services.llm_service import LLMService
import shutil
import os
import uuid

router = APIRouter(prefix="/ingest", tags=["ingestion"])

ingestion_service = IngestionService()
vector_service = VectorService()
graph_service = GraphService()
llm_service = LLMService()

async def process_pdf_background(file_path: str, book_id: str):
    try:
        # 1. Convert PDF to Markdown
        output_dir = f"processed_data/{book_id}"
        md_path = await ingestion_service.convert_pdf_to_markdown(file_path, output_dir)
        
        with open(md_path, "r") as f:
            full_text = f.read()
            
        # 2. Chunking (Simple for now, should be improved)
        # TODO: Use proper chunking from ingestion_service
        chunks = [{"text": chunk} for chunk in full_text.split("\n\n") if len(chunk) > 50]
        
        # 3. Process Chunks
        vector_chunks = []
        for chunk in chunks:
            text = chunk["text"]
            
            # Contextualize (Claude)
            # context = llm_service.contextualize_chunk(text, full_text)
            # enriched_text = f"{context}\n\n{text}"
            enriched_text = text # Skipping for speed in this demo, uncomment above for prod
            
            vector_chunks.append({
                "text": enriched_text,
                "metadata": {"book_id": book_id, "original_text": text}
            })
            
            # Graph Extraction (GPT-4)
            # graph_data = llm_service.extract_graph_entities(text)
            # for node in graph_data.get("nodes", []):
            #     graph_service.add_entity(node["label"], node["properties"])
            # for edge in graph_data.get("edges", []):
            #     graph_service.add_relation(edge["source"], "Node", edge["target"], "Node", edge["type"], edge.get("properties", {}))
                
        # 4. Index in Vector DB
        vector_service.add_chunks(f"book_{book_id}", vector_chunks)
        
        print(f"Successfully processed book {book_id}")
        
    except Exception as e:
        print(f"Error processing book {book_id}: {e}")

@router.post("/upload")
async def upload_pdf(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="File must be a PDF")
        
    book_id = str(uuid.uuid4())
    file_location = f"01_INPUTS/{book_id}_{file.filename}"
    
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    background_tasks.add_task(process_pdf_background, file_location, book_id)
    
    return {"message": "File uploaded and processing started", "book_id": book_id}
