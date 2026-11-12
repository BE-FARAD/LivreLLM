from typing import List
from livrellm.conversion.markdown_document import MarkdownDocument

class TextChunker:
    """Splits document content into chunks."""
    
    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_document(self, doc: MarkdownDocument) -> List[str]:
        chunks = []
        for chapter in doc.chapters:
            # Simple chunking by paragraph or fixed size
            # Here using naive fixed size sliding window on chapter content
            text = chapter.content
            start = 0
            while start < len(text):
                end = start + self.chunk_size
                chunk = text[start:end]
                chunks.append(chunk)
                start += (self.chunk_size - self.overlap)
        return chunks
