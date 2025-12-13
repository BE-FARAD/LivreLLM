import hashlib
from pathlib import Path
from typing import Optional
from config.settings import settings
from .tts_service import TTSService

class AudioManager:
    """Manages audio generation and caching."""
    
    def __init__(self, base_dir: Path = settings.AUDIO_DIR):
        self.base_dir = base_dir
        if not self.base_dir.exists():
            self.base_dir.mkdir(parents=True, exist_ok=True)
        self.tts = TTSService()

    def get_audio_path(self, text: str, book_name: str, chapter_num: int, para_num: int) -> Optional[str]:
        """Returns path to audio file for text, generating it if needed."""
        # Create book subdir
        book_audio_dir = self.base_dir / book_name
        book_audio_dir.mkdir(exist_ok=True)
        
        # Add content hash to filename to differentiate translated versions
        text_hash = hashlib.md5(text.encode()).hexdigest()[:8]
        
        # Naming convention: {nomLivre}_ch{XX}_para{XXX}_{hash}.mp3
        filename = f"{book_name}_ch{chapter_num:02d}_para{para_num:03d}_{text_hash}.mp3"
        file_path = book_audio_dir / filename
        
        if file_path.exists():
            return str(file_path)
            
        # Generate
        print(f"Generating audio for {filename}...")
        audio_content = self.tts.generate_audio(text)
        if audio_content:
            with open(file_path, "wb") as f:
                f.write(audio_content)
            return str(file_path)
            
        return None

    def get_chapter_audio(self, paragraphs_text: list[str], book_name: str, chapter_num: int, progress_callback=None) -> Optional[str]:
        """
        Generates/Retrieves a single audio file for the entire chapter.
        Uses parallel processing for faster generation (up to 5x faster).
        
        Args:
            paragraphs_text: List of paragraph texts
            book_name: Name of the book
            chapter_num: Chapter number
            progress_callback: Optional callback(current, total, status_message)
        """
        book_audio_dir = self.base_dir / book_name
        book_audio_dir.mkdir(exist_ok=True)
        
        # Create a content hash to differentiate between original and translated versions
        content_hash = hashlib.md5("".join(paragraphs_text).encode()).hexdigest()[:8]
        
        full_filename = f"{book_name}_ch{chapter_num:02d}_FULL_{content_hash}.mp3"
        full_file_path = book_audio_dir / full_filename
        
        # If full file exists, return it (cache based on content hash)
        if full_file_path.exists():
            if progress_callback:
                progress_callback(1, 1, "Audio déjà en cache ✅")
            return str(full_file_path)

        # Generate audio files in parallel
        from concurrent.futures import ThreadPoolExecutor, as_completed
        
        # Prepare tasks
        tasks = []
        for i, text in enumerate(paragraphs_text):
            text_hash = hashlib.md5(text.encode()).hexdigest()[:8]
            filename = f"{book_name}_ch{chapter_num:02d}_para{i+1:03d}_{text_hash}.mp3"
            file_path = book_audio_dir / filename
            
            tasks.append({
                'index': i,
                'text': text,
                'path': file_path,
                'needs_generation': not file_path.exists()
            })
        
        # Generate missing audio files in parallel
        total_tasks = len(tasks)
        completed = 0
        
        def generate_single_audio(task):
            """Generate audio for a single paragraph"""
            if not task['needs_generation']:
                return task['index'], task['path'], True
            
            try:
                audio_content = self.tts.generate_audio(task['text'])
                if audio_content:
                    with open(task['path'], "wb") as f:
                        f.write(audio_content)
                    return task['index'], task['path'], True
            except Exception as e:
                print(f"Error generating audio for paragraph {task['index']}: {e}")
            
            return task['index'], None, False
        
        # Use ThreadPoolExecutor for parallel generation
        results = {}
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(generate_single_audio, task): task for task in tasks}
            
            for future in as_completed(futures):
                idx, path, success = future.result()
                results[idx] = (path, success)
                completed += 1
                
                if progress_callback:
                    progress_callback(completed, total_tasks, f"Génération: {completed}/{total_tasks} paragraphes")
        
        # Combine audio files in order
        combined_audio = b""
        for i in range(total_tasks):
            path, success = results.get(i, (None, False))
            if path and path.exists():
                with open(path, "rb") as f:
                    combined_audio += f.read()
        
        if combined_audio:
            with open(full_file_path, "wb") as f:
                f.write(combined_audio)
            
            if progress_callback:
                progress_callback(total_tasks, total_tasks, "Combinaison terminée ✅")
            
            return str(full_file_path)
        
        return None

