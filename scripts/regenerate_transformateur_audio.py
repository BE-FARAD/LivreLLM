
import json
import sys
import os
from pathlib import Path
import hashlib

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from livrellm.storage.audio_manager import AudioManager
from config.settings import settings

def regenerate_audio():
    book_name = "Transformateur_de_Courant"
    json_path = settings.OUTPUT_DIR / book_name / "json" / f"{book_name}.json"
    audio_dir = settings.AUDIO_DIR / book_name
    
    if not audio_dir.exists():
        audio_dir.mkdir(parents=True, exist_ok=True)
        
    print(f"📖 Chargement du livre: {json_path}")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        book_data = json.load(f)
    
    # Init AudioManager (Standard OpenAI)
    audio_manager = AudioManager()
    print("🎤 Utilisation du service audio STANDARD (OpenAI - Alloy)")
    
    total_chapters = len(book_data['chapters'])
    print(f"🔄 Début de la régénération pour {total_chapters} chapitres...")
    
    for chapter in book_data['chapters']:
        chapter_num = chapter['number']
        chapter_title = chapter['title']
        paragraphs = chapter['paragraphs']
        
        print(f"\n🎧 Traitement Chapitre {chapter_num}: {chapter_title} ({len(paragraphs)} paragraphes)")
        
        texts = [p['content'] for p in paragraphs if p['content'].strip()]
        
        try:
            # This calls OpenAI API
            full_audio_path = audio_manager.get_chapter_audio(
                texts, 
                book_name, 
                chapter_num,
                progress_callback=lambda c, t, m: print(f"   Status: {m} ({c}/{t})", end='\r')
            )
            print() # Newline
            
            if full_audio_path:
                print(f"   ✅ Chapitre {chapter_num} terminé: {os.path.basename(full_audio_path)}")
                
                # Update JSON with new filenames
                for i, p in enumerate(paragraphs):
                    text = p['content']
                    if not text.strip():
                        continue
                    
                    text_hash = hashlib.md5(text.encode()).hexdigest()[:8]
                    filename = f"{book_name}_ch{chapter_num:02d}_para{i+1:03d}_{text_hash}.mp3"
                    p['audio_file'] = filename
            else:
                 print(f"   ❌ Chapitre {chapter_num} échoué (Probable erreur API)")

        except Exception as e:
            print(f"   ❌ Erreur critique Chapitre {chapter_num}: {e}")

    # Save updated JSON
    print("\n💾 Sauvegarde du JSON mis à jour...")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(book_data, f, indent=2, ensure_ascii=False)
        
    print("✨ Régénération terminée avec succès!")

if __name__ == "__main__":
    regenerate_audio()
