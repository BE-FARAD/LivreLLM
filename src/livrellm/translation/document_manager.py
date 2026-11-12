from pathlib import Path
from typing import List, Optional
import json
from livrellm.conversion.markdown_document import MarkdownDocument
from config.settings import settings

class DocumentManager:
    """Manages saving and loading of processed documents."""
    
    def __init__(self, output_dir: Path = settings.OUTPUT_DIR):
        self.output_dir = output_dir
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_document(self, doc: MarkdownDocument) -> None:
        """Saves the document metadata and content."""
        book_dir = self.output_dir / doc.book_name / "json"
        book_dir.mkdir(parents=True, exist_ok=True)
        
        # Save as JSON for easy object reconstruction
        json_path = book_dir / f"{doc.book_name}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            f.write(doc.model_dump_json(indent=2))

    def load_document(self, book_name: str) -> Optional[MarkdownDocument]:
        """Loads a document from storage."""
        json_path = self.output_dir / book_name / "json" / f"{book_name}.json"
        if not json_path.exists():
            return None
            
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return MarkdownDocument(**data)

    def list_books(self) -> List[str]:
        """Returns list of processed book names."""
        # Look for dirs in 02-output that contain json/book.json
        books = []
        for d in self.output_dir.iterdir():
            if d.is_dir() and (d / "json" / f"{d.name}.json").exists():
                books.append(d.name)
        return books
