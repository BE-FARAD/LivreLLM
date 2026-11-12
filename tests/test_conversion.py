from livrellm.conversion.marker_converter import MarkerConverter
from livrellm.conversion.markdown_document import MarkdownDocument

def test_marker_converter_structure(tmp_path):
    # Mocking subprocess to avoid real heavy conversion in unit test
    # We test the parsing logic primarily
    
    # Create fake marker output
    d = tmp_path / "output"
    d.mkdir()
    
    book_name = "Test_Book"
    book_dir = d / book_name
    book_dir.mkdir()
    
    md_content = """# Introduction
This is the intro.

# Chapter 1: Basics
Start of chapter 1.

Section 1.1 content.

# Chapter 2: Advanced
Chapter 2 content.
"""
    (book_dir / f"{book_name}.md").write_text(md_content)
    
    # We need to sub-class or mock the convert method to skip subprocess
    # For now, let's test the _parse_chapters logic directly if we can access it, 
    # or assume the user wants an integration test style.
    # Let's rely on the parsing logic which is internal.
    
    converter = MarkerConverter(output_dir=d)
    chapters = converter._parse_chapters(md_content)
    
    assert len(chapters) == 3 # Intro + Chap 1 + Chap 2
    assert chapters[0].title == "Introduction"
    assert chapters[1].title == "Chapter 1: Basics"
    assert len(chapters[1].paragraphs) >= 1

def test_markdown_document_model():
    doc = MarkdownDocument(
        book_name="Test",
        language="en",
        content="raw",
        chapters=[]
    )
    assert doc.book_name == "Test"
