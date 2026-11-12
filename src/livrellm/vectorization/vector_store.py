from typing import List
from .qdrant_client import QdrantClient
from .embedding_service import EmbeddingService
from .text_chunker import TextChunker
from livrellm.conversion.markdown_document import MarkdownDocument

class VectorStore:
    """Facade for Vector Database operations."""
    
    def __init__(self):
        self.client = QdrantClient()
        self.embedding_service = EmbeddingService()
        self.chunker = TextChunker()

    def index_document(self, doc: MarkdownDocument):
        """Indexes an entire document."""
        chunks = self.chunker.split_document(doc)
        if not chunks:
            return
            
        # Batch embedding
        # Process in batches of 32 to avoid mem issues
        batch_size = 32
        for i in range(0, len(chunks), batch_size):
            batch_chunks = chunks[i:i+batch_size]
            vectors = self.embedding_service.embed_batch(batch_chunks)
            
            payloads = [{
                "text": chunk,
                "book_name": doc.book_name,
                "type": "content"
            } for chunk in batch_chunks]
            
            self.client.upsert(vectors, payloads)

    def search(self, query: str, limit: int = 3) -> List[str]:
        """Searches for similar text chunks."""
        query_vector = self.embedding_service.embed(query)
        results = self.client.search(query_vector, limit=limit)
        return [r["text"] for r in results]
