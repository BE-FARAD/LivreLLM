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

def parse_real_chapters(text: str) -> list[Chapter]:
    """
    Parse only real chapters from French book.
    Detects chapters that start with: # **Chapitre X** or # Chapitre X
    """
    lines = text.split('\n')
    chapters = []
    current_content = []
    current_num = 0
    current_title = None
    
    # Regex to detect real chapter headers
    chapter_pattern = re.compile(r'^#\s+\*?\*?Chapitre\s+(\d+)', re.IGNORECASE)
    
    for line in lines:
        match = chapter_pattern.match(line)
        
        if match:
            # Save previous chapter if exists
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
    
    # Add introduction chapter (everything before Chapter 1)
    if chapters and chapters[0].number > 0:
        intro_lines = []
        for line in lines:
            if chapter_pattern.match(line):
                break
            intro_lines.append(line)
        
        if intro_lines:
            intro_text = "\n".join(intro_lines)
            intro_chapter = Chapter(
                number=0,
                title="Introduction et Préface",
                content=intro_text,
                paragraphs=parse_paragraphs(intro_text, 0)
            )
            chapters.insert(0, intro_chapter)
    
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


def reparse_french_book():
    """Re-parse the French book with proper chapter detection."""
    
    # Source file
    source_dir = settings.INPUT_DIR / "The Complete LangGraph Blueprint Build 50+ AI Agents for Business Success"
    md_file = source_dir / "Le Guide Complet LangGraph - Construire 50+ Agents IA.md"
    
    if not md_file.exists():
        print(f"❌ Fichier markdown français introuvable: {md_file}")
        return
    
    print(f"📄 Lecture de {md_file.name}...")
    content = md_file.read_text(encoding="utf-8")
    
    print("🧠 Analyse des chapitres (VRAIES CHAPITRES uniquement)...")
    chapters = parse_real_chapters(content)
    print(f"✅ {len(chapters)} chapitres principaux détectés.")
    
    # Show chapter titles
    print("\n📚 Chapitres détectés:")
    for ch in chapters:
        print(f"   {ch.number}. {ch.title[:60]}...")
    
    # Book name (normalized)
    book_name = "Le_Guide_Complet_LangGraph"
    
    # Create document with language="fr"
    doc = MarkdownDocument(
        book_name=book_name,
        language="fr",  # ✅ IMPORTANT: Français!
        content=content,
        chapters=chapters,
        file_path=str(md_file)
    )
    
    # Save document
    dm = DocumentManager()
    print("\n💾 Sauvegarde du document...")
    dm.save_document(doc)
    
    # Copy images to output directory
    output_images_dir = settings.OUTPUT_DIR / book_name
    output_images_dir.mkdir(parents=True, exist_ok=True)
    
    print("📸 Copie des images...")
    image_count = 0
    for img_file in source_dir.glob("*.jpeg"):
        dest = output_images_dir / img_file.name
        if not dest.exists():  # Don't recopy if exists
            shutil.copy2(img_file, dest)
        image_count += 1
    
    print(f"✅ {image_count} images disponibles.")
    print(f"\n🎉 Livre '{book_name}' réimporté avec succès!")
    print(f"📊 {len(chapters)} chapitres principaux au lieu de 630 sections!")
    print("📱 Rafraîchissez votre navigateur pour voir les changements.")

if __name__ == "__main__":
    reparse_french_book()
