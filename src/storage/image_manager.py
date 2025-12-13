import os
from pathlib import Path
from PIL import Image
from config.settings import settings

class ImageManager:
    """Manages storage and retrieval of images extracted from books."""
    
    def __init__(self, base_directory: Path = settings.IMAGES_DIR):
        self.base_directory = base_directory
        if not self.base_directory.exists():
            self.base_directory.mkdir(parents=True, exist_ok=True)
            
    def get_book_image_dir(self, book_name: str) -> Path:
        """Returns the directory for a specific book's images."""
        d = self.base_directory / book_name
        d.mkdir(exist_ok=True)
        return d

    def save_image(self, image_path: Path, book_name: str) -> Optional[str]:
        """Moves/Saves an image to the managed directory."""
        if not image_path.exists():
            return None
            
        target_dir = self.get_book_image_dir(book_name)
        target_path = target_dir / image_path.name
        
        # In a real app, we might move or copy. For now, copy.
        import shutil
        shutil.copy2(image_path, target_path)
        
        # Return relative path for storage in DB/frontend
        return str(target_path.relative_to(settings.DATA_DIR))
