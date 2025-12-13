"""
Script pour générer TOUS les audios manquants pour TOUS les livres français.
"""

import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from src.translation.document_manager import DocumentManager
from src.reading.reading_session_manager import ReadingSessionManager
from config.settings import settings


def generate_chapter_audio(book_name: str, chapter_num: int, chapter_title: str, paragraphs: list, rsm: ReadingSessionManager):
    """Generate audio for a single chapter."""
    try:
        print(f"   🎧 Chapitre {chapter_num}: {chapter_title[:60]}...")
        
        # Extract text from paragraphs
        texts = [p.content for p in paragraphs if p.content.strip()]
        
        if not texts:
            print(f"   ⚠️  Chapitre {chapter_num} vide, ignoré")
            return False
        
        # Generate audio
        audio_path = rsm.audio_manager.get_chapter_audio(
            texts,
            book_name,
            chapter_num
        )
        
        if audio_path:
            print(f"   ✅ Audio créé pour Chapitre {chapter_num}")
            return True
        else:
            print(f"   ❌ Échec audio Chapitre {chapter_num}")
            return False
            
    except Exception as e:
        print(f"   ❌ Erreur Chapitre {chapter_num}: {e}")
        return False


def generate_book_audios(doc):
    """Generate all audios for a single book."""
    print(f"\n🎵 Génération des audios pour '{doc.book_name}'")
    print("=" * 80)
    print(f"📊 {len(doc.chapters)} chapitres à traiter")
    print("⚡ Utilisation du traitement parallèle (3 workers)\n")
    
    rsm = ReadingSessionManager()
    success_count = 0
    fail_count = 0
    
    # Use ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit all chapters
        future_to_chapter = {
            executor.submit(
                generate_chapter_audio, 
                doc.book_name, 
                chapter.number, 
                chapter.title,
                chapter.paragraphs,
                rsm
            ): chapter
            for chapter in doc.chapters
        }
        
        # Process as they complete
        for future in as_completed(future_to_chapter):
            chapter = future_to_chapter[future]
            try:
                success = future.result()
                if success:
                    success_count += 1
                else:
                    fail_count += 1
            except Exception as e:
                print(f"   ❌ Exception Chapitre {chapter.number}: {e}")
                fail_count += 1
    
    print(f"\n📊 Résumé pour {doc.book_name}:")
    print(f"   ✅ Réussis: {success_count}/{len(doc.chapters)}")
    print(f"   ❌ Échecs: {fail_count}")
    print(f"   📁 Dossier audio: {settings.AUDIO_DIR / doc.book_name}\n")
    
    return success_count, fail_count


def main():
    """Main processing function."""
    print("\n" + "=" * 80)
    print("🚀 GÉNÉRATION DE TOUS LES AUDIOS")
    print("=" * 80)
    
    dm = DocumentManager()
    
    # List of books to process
    book_names = [
        "Le_Guide_Complet_LangGraph",
        "Apprendre_LangChain",
        "Transformateur_de_Courant"
    ]
    
    total_success = 0
    total_fail = 0
    total_books = 0
    
    for book_name in book_names:
        try:
            # Load document
            doc = dm.load_document(book_name)
            if doc is None:
                print(f"❌ Livre '{book_name}' introuvable, ignoré")
                continue
            
            print(f"\n📚 Livre: {book_name}")
            print(f"📖 Chapitres: {len(doc.chapters)}")
            
            # Generate audios
            success, fail = generate_book_audios(doc)
            total_success += success
            total_fail += fail
            total_books += 1
            
        except Exception as e:
            print(f"❌ Erreur pour {book_name}: {e}")
            import traceback
            traceback.print_exc()
    
    # Final summary
    print("\n" + "=" * 80)
    print("🎉 GÉNÉRATION TERMINÉE!")
    print("=" * 80)
    print(f"📚 {total_books} livres traités")
    print(f"✅ {total_success} audios générés avec succès")
    print(f"❌ {total_fail} échecs")
    print(f"📁 Tous les audios dans: {settings.AUDIO_DIR}")
    print("\n💡 Vous pouvez maintenant utiliser l'application HORS LIGNE!")
    print("📱 Rafraîchissez votre navigateur si besoin.")


if __name__ == "__main__":
    main()
