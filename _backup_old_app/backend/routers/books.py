from fastapi import APIRouter
import os

router = APIRouter(prefix="/books", tags=["books"])

PROCESSED_DIR = "processed_data"

@router.get("/")
async def list_books():
    if not os.path.exists(PROCESSED_DIR):
        return []
    
    books = []
    for book_id in os.listdir(PROCESSED_DIR):
        # Assuming directory name is book_id
        # We could read a metadata.json inside to get the title
        books.append({"id": book_id, "title": book_id})
        
    return books
