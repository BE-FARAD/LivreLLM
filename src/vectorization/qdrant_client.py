from typing import List, Dict, Any, Optional
from uuid import uuid4
from qdrant_client import QdrantClient as QClient
from qdrant_client.http import models
from config.settings import settings

class QdrantClient:
    """Wrapper around Qdrant QClient for the project."""
    
    def __init__(self):
        # Prefer local disk path for stability if user doesn't have Docker
        # Using 'local_qdrant_db' like current app did
        self.path = "local_qdrant_db"
        self.client = QClient(path=self.path)
        self.collection_name = "book_chunks"
        self.vector_size = 384 # BAAI/bge-small-en-v1.5 size

        self._ensure_collection()

    def _ensure_collection(self):
        try:
            collections = self.client.get_collections().collections
            if not any(c.name == self.collection_name for c in collections):
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=models.VectorParams(
                        size=self.vector_size, 
                        distance=models.Distance.COSINE
                    )
                )
        except Exception as e:
            print(f"Qdrant Init Warning: {e}")

    def upsert(self, vectors: List[List[float]], payloads: List[Dict[str, Any]]):
        points = []
        for vec, payload in zip(vectors, payloads):
            points.append(models.PointStruct(
                id=str(uuid4()),
                vector=vec,
                payload=payload
            ))
        
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

    def search(self, query_vector: List[float], limit: int = 5) -> List[Dict[str, Any]]:
        hits = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=limit
        )
        return [hit.payload for hit in hits]
