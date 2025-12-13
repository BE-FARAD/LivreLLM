import os
import uuid
import json
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http import models
from fastembed import TextEmbedding

load_dotenv()

# Config
LIBRARY_DIR = "library_data"
COLLECTION_NAME = "books_collection"

print("Initializing DB...")
client = QdrantClient(path="local_qdrant_db")
embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Ensure collection exists
try:
    collections = client.get_collections().collections
    exists = any(c.name == COLLECTION_NAME for c in collections)
    if not exists:
         client.create_collection(
             collection_name=COLLECTION_NAME,
             vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE)
         )
except Exception as e:
    print(f"Collection check error (ignoring): {e}")

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += (chunk_size - overlap)
    return chunks

def index_book(book_id):
    book_dir = os.path.join(LIBRARY_DIR, book_id)
    md_path = os.path.join(book_dir, "content.md")
    
    if not os.path.exists(md_path):
        return

    print(f"Indexing {book_id}...")
    with open(md_path, "r") as f:
        text = f.read()
        
    chunks = chunk_text(text)
    print(f"  - {len(chunks)} chunks to embed")
    
    # Embed in batches
    batch_size = 32
    for i in range(0, len(chunks), batch_size):
        batch_chunks = chunks[i:i+batch_size]
        batch_vectors = list(embedding_model.embed(batch_chunks))
        
        points = []
        for chunk, vector in zip(batch_chunks, batch_vectors):
            points.append(models.PointStruct(
                id=str(uuid.uuid4()),
                vector=vector.tolist(),
                payload={"text": chunk, "filename": book_id} # Storing book_id as filename for filtering if needed
            ))
        
        client.upsert(collection_name=COLLECTION_NAME, points=points)
        print(f"    Batch {i//batch_size + 1} done")

    print(f"Done indexing {book_id}")

# Main loop
if os.path.exists(LIBRARY_DIR):
    for book_id in os.listdir(LIBRARY_DIR):
        if os.path.isdir(os.path.join(LIBRARY_DIR, book_id)):
            try:
                index_book(book_id)
            except Exception as e:
                print(f"Error indexing {book_id}: {e}")

print("All done.")
