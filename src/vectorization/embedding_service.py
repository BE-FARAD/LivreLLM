from typing import List
from fastembed import TextEmbedding

class EmbeddingService:
    """Handles text embedding using FastEmbed (local)."""
    
    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5"):
        self.model_name = model_name
        self._model = TextEmbedding(model_name=self.model_name)

    def embed(self, text: str) -> List[float]:
        """Embeds a single string."""
        # FastEmbed returns a generator of vectors
        vectors = list(self._model.embed([text]))
        return vectors[0].tolist()

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Embeds a batch of strings."""
        return [v.tolist() for v in self._model.embed(texts)]
