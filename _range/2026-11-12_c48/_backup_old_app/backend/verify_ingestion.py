import sys
import os

sys.path.append(os.getcwd())

from backend.services.rag_service import RAGService

def verify():
    rag = RAGService()
    # Query for something likely to be in a forecasting book
    query = "forecasting"
    book_id = "91b6b1d4-a4e7-4b53-bf1d-6e3130772bfe"
    
    print(f"Querying for '{query}' in book '{book_id}'...")
    results = rag.query(query, book_id=book_id)
    
    if results:
        print("Found results:")
        for res in results:
            print(f"- {res[:100]}...")
    else:
        print("No results found.")

if __name__ == "__main__":
    verify()
