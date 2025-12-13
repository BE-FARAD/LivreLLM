"""
Script pour traiter TOUS les livres français et générer les audios automatiquement.
Ce script permet une utilisation hors ligne en pré-générant tous les audios.
"""

import sys
import re
from pathlib import Path
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from src.conversion.markdown_document import MarkdownDocument
from src.conversion.chapter import Chapter, Paragraph
from src.translation.document_manager import DocumentManager
from src.reading.reading_session_manager import ReadingSessionManager
from config.settings import settings


def parse_chapters_langgraph(text: str) -> list[Chapter]:
    """Parse chapters for LangGraph book: # **Chapitre X**"""
    lines = text.split('\n')
    chapters = []
    current_content = []
    current_num = 0
    current_title = None
    
    # Pattern for: # **Chapitre X**
    pattern = re.compile(r'^#\s+\*?\*?Chapitre\s+(\d+)', re.IGNORECASE)
    
    for line in lines:
        match = pattern.match(line)
        
        if match:
            # Save previous chapter
            if current_content and current_title:
                full_text = "\n".join(current_content)
                chapters.append(Chapter(
                    number=current_num,
                    title=current_title,
                    content=full_text,
                    paragraphs=parse_paragraphs(full_text, current_num)
                ))
            
            # Start new chapter
            current_num = int(match.group(1))
            current_title = line.replace("#", "").replace("*", "").strip()
            current_content = [line]
        else:
            current_content.append(line)
    
    # Save last chapter
    if current_content and current_title:
        full_text = "\n".join(current_content)
        chapters.append(Chapter(
            number=current_num,
            title=current_title,
            content=full_text,
            paragraphs=parse_paragraphs(full_text, current_num)
        ))
    
    # Add introduction
    if chapters and chapters[0].number > 0:
        intro_lines = []
        for line in lines:
            if pattern.match(line):
                break
            intro_lines.append(line)
        
        if intro_lines:
            intro_text = "\n".join(intro_lines)
            chapters.insert(0, Chapter(
                number=0,
                title="Introduction et Préface",
                content=intro_text,
                paragraphs=parse_paragraphs(intro_text, 0)
            ))
    
    return chapters


def parse_chapters_langchain(text: str) -> list[Chapter]:
    """Parse chapters for LangChain book: # <span>...</span>Chapitre X. Title"""
    lines = text.split('\n')
    chapters = []
    current_content = []
    current_num = 0
    current_title = None
    
    # Pattern with optional HTML span - accept both # and ## headers
    pattern = re.compile(r'^#{1,2}\s+(?:\<span[^\>]*\>\</span\>)?\*?\*?Chapitre\s+(\d+)[\.\:]?\s*(.*)$', re.IGNORECASE)
    
    for line in lines:
        match = pattern.match(line)
        
        if match:
            # Save previous chapter
            if current_content and current_title:
                full_text = "\n".join(current_content)
                chapters.append(Chapter(
                    number=current_num,
                    title=current_title,
                    content=full_text,
                    paragraphs=parse_paragraphs(full_text, current_num)
                ))
            
            # Start new chapter
            current_num = int(match.group(1))
            # Clean title from HTML tags
            title = line.replace("#", "").strip()
            title = re.sub(r'<span[^>]*>.*?</span>', '', title).strip()
            title = title.replace("*", "").strip()
            current_title = title
            current_content = [line]
        else:
            current_content.append(line)
    
    # Save last chapter
    if current_content and current_title:
        full_text = "\n".join(current_content)
        chapters.append(Chapter(
            number=current_num,
            title=current_title,
            content=full_text,
            paragraphs=parse_paragraphs(full_text, current_num)
        ))
    
    # Add introduction
    if chapters and chapters[0].number > 0:
        intro_lines = []
        for line in lines:
            if pattern.match(line):
                break
            intro_lines.append(line)
        
        if intro_lines:
            intro_text = "\n".join(intro_lines)
            chapters.insert(0, Chapter(
                number=0,
                title="Introduction et Préface",
                content=intro_text,
                paragraphs=parse_paragraphs(intro_text, 0)
            ))
    
    return chapters


def parse_paragraphs(chapter_text: str, chapter_num: int) -> list[Paragraph]:
    """Splits chapter text into logical paragraphs."""
    raw_paras = chapter_text.split('\n\n')
    paras = []
    p_num = 1
    for p in raw_paras:
        if p.strip():
            paras.append(Paragraph(
                number=p_num,
                content=p.strip()
            ))
            p_num += 1
    return paras


def import_book(md_file: Path, book_name: str, parser_func) -> MarkdownDocument:
    """Import a single book with specified parser."""
    print(f"\n📄 Traitement : {md_file.name}")
    print("=" * 80)
    
    content = md_file.read_text(encoding="utf-8")
    
    print("🧠 Analyse des chapitres...")
    chapters = parser_func(content)
    print(f"✅ {len(chapters)} chapitres détectés")
    
    # Show chapters
    print("\n📚 Chapitres:")
    for ch in chapters[:10]:
        print(f"   {ch.number}. {ch.title[:70]}")
    if len(chapters) > 10:
        print(f"   ... et {len(chapters) - 10} autres chapitres")
    
    # Create document
    doc = MarkdownDocument(
        book_name=book_name,
        language="fr",
        content=content,
        chapters=chapters,
        file_path=str(md_file)
    )
    
    # Save
    dm = DocumentManager()
    print(f"\n💾 Sauvegarde...")
    dm.save_document(doc)
    
    # Copy images
    source_dir = md_file.parent
    output_images_dir = settings.OUTPUT_DIR / book_name
    output_images_dir.mkdir(parents=True, exist_ok=True)
    
    image_count = 0
    for ext in ['*.jpeg', '*.jpg', '*.png', '*.gif']:
        for img_file in source_dir.glob(ext):
            dest = output_images_dir / img_file.name
            if not dest.exists():
                shutil.copy2(img_file, dest)
            image_count += 1
    
    if image_count > 0:
        print(f"📸 {image_count} images copiées")
    
    print(f"✅ '{book_name}' traité avec succès!\n")
    return doc


def generate_chapter_audio(book_name: str, chapter: Chapter, rsm: ReadingSessionManager):
    """Generate audio for a single chapter."""
    try:
        print(f"   🎧 Génération audio Chapitre {chapter.number}: {chapter.title[:50]}...")
        
        # Extract text from paragraphs
        texts = [p.content for p in chapter.paragraphs if p.content.strip()]
        
        # Generate audio
        audio_path = rsm.audio_manager.get_chapter_audio(
            texts,
            book_name,
            chapter.number
        )
        
        if audio_path:
            print(f"   ✅ Audio créé pour Chapitre {chapter.number}")
            return True
        else:
            print(f"   ❌ Échec audio Chapitre {chapter.number}")
            return False
            
    except Exception as e:
        print(f"   ❌ Erreur Chapitre {chapter.number}: {e}")
        return False


def generate_all_audios(doc: MarkdownDocument):
    """Generate audio for all chapters of a book using parallel processing."""
    print(f"\n🎵 Génération des audios pour '{doc.book_name}'")
    print("=" * 80)
    print(f"📊 {len(doc.chapters)} chapitres à traiter")
    print("⚡ Utilisation du traitement parallèle (5 workers)\n")
    
    rsm = ReadingSessionManager()
    success_count = 0
    fail_count = 0
    
    # Use ThreadPoolExecutor for parallel processing (5 workers like in audio_manager)
    with ThreadPoolExecutor(max_workers=3) as executor:  # 3 workers to avoid rate limits
        # Submit all chapters
        future_to_chapter = {
            executor.submit(generate_chapter_audio, doc.book_name, chapter, rsm): chapter
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
    
    print(f"\n📊 Résumé:")
    print(f"   ✅ Réussis: {success_count}")
    print(f"   ❌ Échecs: {fail_count}")
    print(f"   📁 Dossier audio: {settings.AUDIO_DIR / doc.book_name}")


def main():
    """Main processing function."""
    print("\n" + "=" * 80)
    print("🚀 TRAITEMENT DE TOUS LES LIVRES FRANÇAIS")
    print("=" * 80)
    
    # Book configurations
    books = [
        {
            "file": settings.INPUT_DIR / "The Complete LangGraph Blueprint Build 50+ AI Agents for Business Success" / "Le Guide Complet LangGraph - Construire 50+ Agents IA.md",
            "name": "Le_Guide_Complet_LangGraph",
            "parser": parse_chapters_langgraph
        },
        {
            "file": settings.INPUT_DIR / "Learning LangChain Building" / "Apprendre LangChain - Construire des Applications IA et LLM.md",
            "name": "Apprendre_LangChain",
            "parser": parse_chapters_langchain
        }
    ]
    
    processed_books = []
    
    # Step 1: Import all books
    print("\n📚 ÉTAPE 1/2 : IMPORTATION DES LIVRES")
    print("=" * 80)
    
    for book_config in books:
        if not book_config["file"].exists():
            print(f"❌ Fichier introuvable: {book_config['file']}")
            continue
        
        try:
            doc = import_book(
                book_config["file"],
                book_config["name"],
                book_config["parser"]
            )
            processed_books.append(doc)
        except Exception as e:
            print(f"❌ Erreur lors de l'importation de {book_config['name']}: {e}")
    
    # Step 2: Generate all audios
    print("\n🎵 ÉTAPE 2/2 : GÉNÉRATION DES AUDIOS")
    print("=" * 80)
    print("⚠️  Cela peut prendre du temps selon le nombre de chapitres...")
    print("💡 Les audios permettent l'écoute hors ligne!\n")
    
    for doc in processed_books:
        try:
            generate_all_audios(doc)
        except Exception as e:
            print(f"❌ Erreur génération audio pour {doc.book_name}: {e}")
    
    # Summary
    print("\n" + "=" * 80)
    print("🎉 TRAITEMENT TERMINÉ!")
    print("=" * 80)
    print(f"📚 {len(processed_books)} livres traités")
    print(f"📁 Emplacement: {settings.OUTPUT_DIR}")
    print(f"🎧 Audios: {settings.AUDIO_DIR}")
    print("\n💡 Vous pouvez maintenant utiliser l'application HORS LIGNE!")
    print("📱 Rafraîchissez votre navigateur pour voir les livres.")


if __name__ == "__main__":
    main()
