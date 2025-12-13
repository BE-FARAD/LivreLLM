"""
Script final pour importer TOUS les livres français avec parsing corrigé.
"""

import sys
import re
from pathlib import Path
import shutil

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from src.conversion.markdown_document import MarkdownDocument
from src.conversion.chapter import Chapter, Paragraph
from src.translation.document_manager import DocumentManager
from config.settings import settings


def parse_chapters_langgraph(text: str) -> list[Chapter]:
    """Parse chapters for LangGraph book: # **Chapitre X**"""
    lines = text.split('\n')
    chapters = []
    current_content = []
    current_num = 0
    current_title = None
    
    pattern = re.compile(r'^#\s+\*?\*?Chapitre\s+(\d+)', re.IGNORECASE)
    
    for line in lines:
        match = pattern.match(line)
        
        if match:
            if current_content and current_title:
                full_text = "\n".join(current_content)
                chapters.append(Chapter(
                    number=current_num,
                    title=current_title,
                    content=full_text,
                    paragraphs=parse_paragraphs(full_text, current_num)
                ))
            
            current_num = int(match.group(1))
            current_title = line.replace("#", "").replace("*", "").strip()
            current_content = [line]
        else:
            current_content.append(line)
    
    if current_content and current_title:
        full_text = "\n".join(current_content)
        chapters.append(Chapter(
            number=current_num,
            title=current_title,
            content=full_text,
            paragraphs=parse_paragraphs(full_text, current_num)
        ))
    
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
    """Parse chapters for LangChain book: # or ## <span>...</span>Chapitre X. Title"""
    lines = text.split('\n')
    chapters = []
    current_content = []
    current_num = 0
    current_title = None
    
    # Accept both # and ## headers
    pattern = re.compile(r'^#{1,2}\s+(?:\<span[^\>]*\>\</span\>)?\*?\*?Chapitre\s+(\d+)[\.\:]?\s*(.*)$', re.IGNORECASE)
    
    for line in lines:
        match = pattern.match(line)
        
        if match:
            if current_content and current_title:
                full_text = "\n".join(current_content)
                chapters.append(Chapter(
                    number=current_num,
                    title=current_title,
                    content=full_text,
                    paragraphs=parse_paragraphs(full_text, current_num)
                ))
            
            current_num = int(match.group(1))
            title = line.replace("#", "").strip()
            title = re.sub(r'<span[^>]*>.*?</span>', '', title).strip()
            title = title.replace("*", "").strip()
            current_title = title
            current_content = [line]
        else:
            current_content.append(line)
    
    if current_content and current_title:
        full_text = "\n".join(current_content)
        chapters.append(Chapter(
            number=current_num,
            title=current_title,
            content=full_text,
            paragraphs=parse_paragraphs(full_text, current_num)
        ))
    
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


def parse_simple_document(text: str) -> list[Chapter]:
    """Parse documents without explicit chapters - treat as single chapter"""
    # For documents like "Transformateur de courant" that don't have chapters
    return [
        Chapter(
            number=1,
            title="Document complet",
            content=text,
            paragraphs=parse_paragraphs(text, 1)
        )
    ]


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
    
    print("🧠 Analyse du contenu...")
    chapters = parser_func(content)
    print(f"✅ {len(chapters)} chapitres détectés")
    
    # Show chapters
    print("\n📚 Chapitres:")
    for ch in chapters[:15]:
        print(f"   {ch.number}. {ch.title[:70]}")
    if len(chapters) > 15:
        print(f"   ... et {len(chapters) - 15} autres chapitres")
    
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


def main():
    """Main processing function."""
    print("\n" + "=" * 80)
    print("🚀 IMPORT DE TOUS LES LIVRES FRANÇAIS")
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
        },
        {
            "file": settings.INPUT_DIR / "Transformateur de courant" / "Transformateur de courant.md",
            "name": "Transformateur_de_Courant",
            "parser": parse_simple_document
        }
    ]
    
    processed_books = []
    
    print("\n📚 IMPORTATION DES LIVRES")
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
            import traceback
            traceback.print_exc()
    
    # Summary
    print("\n" + "=" * 80)
    print("🎉 IMPORT TERMINÉ!")
    print("=" * 80)
    print(f"📚 {len(processed_books)} livres importés")
    print(f"📁 Emplacement: {settings.OUTPUT_DIR}")
    print("\n📱 Rafraîchissez votre navigateur pour voir tous les livres.")


if __name__ == "__main__":
    main()
