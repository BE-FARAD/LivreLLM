import hashlib
from pathlib import Path
from typing import List, Dict
from config.settings import settings

class FileWatcher:
    def __init__(self, input_directory: Path = settings.INPUT_DIR):
        self.input_directory = input_directory
        if not self.input_directory.exists():
            self.input_directory.mkdir(parents=True, exist_ok=True)

    def scan_directory(self) -> List[Path]:
        """Scans the input directory for PDF files."""
        return list(self.input_directory.glob("*.pdf"))

    def compute_hash(self, file_path: Path) -> str:
        """Computes SHA-256 hash of the file content."""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            # Read in chunks to handle large files
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def get_new_files(self) -> List[Dict[str, str]]:
        """
        Returns a list of files found in the input directory.
        Format: [{'path': '/path/to/file.pdf', 'hash': 'sha256...'}]
        """
        files = self.scan_directory()
        results = []
        for file in files:
            file_hash = self.compute_hash(file)
            results.append({
                "path": str(file),
                "filename": file.name,
                "hash": file_hash
            })
        return results

    def validate_pdf(self, file_path: Path) -> bool:
        """Basic validation to check if file ends with .pdf and is not empty."""
        return file_path.suffix.lower() == ".pdf" and file_path.stat().st_size > 0
