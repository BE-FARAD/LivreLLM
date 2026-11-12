from typing import List, Dict
from livrellm.conversion.chapter import Chapter
from livrellm.storage.audio_manager import AudioManager

class ReadingSessionManager:
    """Manages the logic of a reading session."""
    
    def __init__(self):
        self.audio_manager = AudioManager()
        # In a real app, we'd inject Dependencies, but keeping it simple
        
    def get_chapter_audio(self, book_name: str, chapter: Chapter) -> List[Dict]:
        """
        Prepares audio for an entire chapter.
        Returns a list of segments: [{'text': '...', 'audio_path': '...', 'paragraph_num': 1}]
        """
        segments = []
        for p in chapter.paragraphs:
            # Skip empty paragraphs
            if not p.content.strip():
                continue
                
            path = self.audio_manager.get_audio_path(p.content, book_name, chapter.number, p.number)
            segments.append({
                "paragraph_num": p.number,
                "text": p.content,
                "audio_path": path
            })
        return segments
