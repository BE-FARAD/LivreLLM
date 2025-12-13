import sys
from pathlib import Path
import re

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from src.conversion.marker_converter import MarkerConverter
from src.conversion.markdown_document import MarkdownDocument
from src.translation.document_manager import DocumentManager
from config.settings import settings

def reparse_book():
    # Use existing markdown file
    md_file = settings.INPUT_DIR / "Learning LangChain Building" / "Learning LangChain Building AI and LLM Applications with LangChain and LangGraph (Mayo Oshin, Nuno Campos) (Z-Library).md"
    
    if not md_file.exists():
        print(f"❌ Markdown file not found: {md_file}")
        return
        
    print(f"📄 Reading {md_file.name}...")
    content = md_file.read_text(encoding="utf-8")
    
    # Use updated converter logic
    converter = MarkerConverter()
    
    print("🧠 Reparsing chapters with improved logic...")
    chapters = converter._parse_chapters(content)
    print(f"✅ Parsed {len(chapters)} logical chapters/sections.")
    
    book_name = "Learning_LangChain_Building"
    
    doc = MarkdownDocument(
        book_name=book_name,
        language="en",
        content=content,
        chapters=chapters,
        file_path=str(md_file)
    )
    
    # Save
    dm = DocumentManager()
    print("💾 Updates document JSON...")
    dm.save_document(doc)
    print("🎉 Done! Refresh Streamlit to see changes.")

if __name__ == "__main__":
    reparse_book()
