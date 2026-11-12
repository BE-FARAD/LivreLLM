from typing import List, Optional
from pydantic import BaseModel
from .chapter import Chapter

class MarkdownDocument(BaseModel):
    """Represents a fully converted markdown document."""
    book_name: str
    language: str
    content: str  # Full raw content
    chapters: List[Chapter] = []
    metadata: dict = {}
    file_path: Optional[str] = None

    def get_chapter(self, number: int) -> Optional[Chapter]:
        for ch in self.chapters:
            if ch.number == number:
                return ch
        return None
