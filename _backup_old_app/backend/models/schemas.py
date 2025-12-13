from pydantic import BaseModel
from typing import List, Tuple

class Word(BaseModel):
    text: str
    rect: Tuple[float, float, float, float] # x0, y0, x1, y1

class Sentence(BaseModel):
    text: str
    words: List[Word]

class PageData(BaseModel):
    page: int
    width: float
    height: float
    sentences: List[Sentence]

class BookResponse(BaseModel):
    id: str
    title: str
    pages: List[PageData]
