import pytest
from src.vectorization.text_chunker import TextChunker
from src.conversion.markdown_document import MarkdownDocument
from src.conversion.chapter import Chapter

def test_chunking_logic():
    # Setup doc
    chap = Chapter(
        number=1, 
        title="Test", 
        content="A" * 1000, # 1000 chars
        paragraphs=[]
    )
    doc = MarkdownDocument(book_name="T", language="en", content="", chapters=[chap])
    
    chunker = TextChunker(chunk_size=500, overlap=0)
    chunks = chunker.split_document(doc)
    
    assert len(chunks) == 2
    assert len(chunks[0]) == 500
    assert len(chunks[1]) == 500

def test_chunking_overlap():
    content = "0123456789"
    chap = Chapter(number=1, title="T", content=content, paragraphs=[])
    doc = MarkdownDocument(book_name="T", language="en", content="", chapters=[chap])
    
    # chunk 5, overlap 2
    # 01234
    #    34567
    #       6789 (short)
    chunker = TextChunker(chunk_size=5, overlap=2)
    chunks = chunker.split_document(doc)
    
    assert chunks[0] == "01234"
    assert chunks[1] == "34567"
    assert chunks[2] == "6789"
