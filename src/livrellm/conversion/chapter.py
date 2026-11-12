from typing import List, Optional
from pydantic import BaseModel

class Paragraph(BaseModel):
    """Represents a single paragraph in a chapter."""
    number: int
    content: str
    
class Chapter(BaseModel):
    """Represents a chapter in a book."""
    number: int
    title: str
    content: str
    paragraphs: List[Paragraph] = []

    def get_paragraph(self, number: int) -> Optional[Paragraph]:
        for p in self.paragraphs:
            if p.number == number:
                return p
        return None
