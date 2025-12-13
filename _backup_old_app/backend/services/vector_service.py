from qdrant_client import QdrantClient
from qdrant_client.http import models
import os
from typing import List, Dict, Any
import uuid

# Global client instance to avoid locking issues with multiple service instantiations
_qdrant_client_instance = None

class VectorService:
    def __init__(self):
        global _qdrant_client_instance
        
        # Initialize Qdrant Client
        # For local development, we can use memory or a local path.
        # For production, this should be a URL.
        if _qdrant_client_instance is None:
            _qdrant_client_instance = QdrantClient(path="qdrant_db") # Local persistence
        
        self.client = _qdrant_client_instance
        
        # Use FastEmbed for local embeddings
        from fastembed import TextEmbedding
        self.embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
        # vector_size for BAAI/bge-small-en-v1.5 is 384
        self.vector_size = 384 
        
    def _get_embedding(self, text: str) -> List[float]:
        text = text.replace("\n", " ")
        # FastEmbed returns a generator, we take the first item
        return list(self.embedding_model.embed([text]))[0]

    def create_collection_if_not_exists(self, collection_name: str):
        if not self.client.collection_exists(collection_name):
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(size=self.vector_size, distance=models.Distance.COSINE),
            )

    def add_chunks(self, collection_name: str, chunks: List[Dict[str, Any]]):
        """
        Adds chunks to the Qdrant collection.
        chunks: List of dicts with 'text', 'metadata', etc.
        """
        self.create_collection_if_not_exists(collection_name)
        
        points = []
        for chunk in chunks:
            text = chunk["text"]
            # If we have contextualized text, we might want to embed that instead
            # For now assuming 'text' is what we want to embed
            
            vector = self._get_embedding(text)
            
            payload = chunk.get("metadata", {})
            payload["text"] = text # Store text in payload for retrieval
            
            points.append(models.PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload=payload
            ))
            
        self.client.upsert(
            collection_name=collection_name,
            points=points
        )

    def search(self, collection_name: str, query_text: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Search for relevant chunks in Qdrant.
        """
        if not self.client.collection_exists(collection_name):
            return []

        query_vector = self._get_embedding(query_text)
        
        search_result = self.client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            limit=limit
        )
        
        results = []
        for hit in search_result:
            results.append({
                "text": hit.payload.get("text"),
                "score": hit.score,
                "metadata": {k:v for k,v in hit.payload.items() if k != "text"}
            })
            
        return results
