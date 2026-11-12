import sys
import re
from pathlib import Path
import shutil

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from livrellm.conversion.markdown_document import MarkdownDocument
from livrellm.conversion.chapter import Chapter, Paragraph
from livrellm.translation.document_manager import DocumentManager
from config.settings import settings


def parse_chapters_langchain(text: str) -> list[Chapter]:
    """Parse chapters for LangChain book: # or ## <span>...</span>Chapitre X. Title"""
    lines = text.split('\n')
    chapters = []
    current_content = []
    current_num = 0
    current_title = None
    
    # Pattern with optional HTML span - accept both # and ## headers
    # Also handles HTML spans like: # <span id="..."></span>Chapitre X. Title
    pattern = re.compile(r'^#{1,2}\s+(?:\<span[^\>]*\>\</span\>)?\*?\*?Chapitre\s+(\d+)[\.\:]?\s*(.*)$', re.IGNORECASE)

    # Un seul motif aujourd'hui, mais les deux boucles plus bas parcourent une
    # liste : elles etaient ecrites pour `patterns`, qui n'a jamais ete defini.
    # Ce script levait donc `NameError` des la premiere ligne lue — il n'a
    # jamais pu tourner (C48, phase 0). On donne a la liste le motif qui
    # existe, plutot que d'inventer ceux qui manquaient peut-etre.
    patterns = [pattern]

    for line in lines:
        match = None
        chapter_num = None
        
        # Try each pattern
        for pattern in patterns:
            match = pattern.match(line)
            if match:
                if len(match.groups()) >= 1:
                    chapter_num = int(match.group(1))
                break
        
        if match and chapter_num:
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
            current_num = chapter_num
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
        found_first_chapter = False
        for line in lines:
            # Check if this is the first real chapter
            for pattern in patterns:
                if pattern.match(line):
                    found_first_chapter = True
                    break
            if found_first_chapter:
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


def import_learning_langchain():
    """Import the French LangChain book."""
    
    # Source file
    source_dir = settings.INPUT_DIR / "Learning LangChain Building"
    md_file = source_dir / "Apprendre LangChain - Construire des Applications IA et LLM.md"
    
    if not md_file.exists():
        print(f"❌ Fichier markdown introuvable: {md_file}")
        return
    
    print(f"📄 Lecture de {md_file.name}...")
    content = md_file.read_text(encoding="utf-8")
    
    print("🧠 Analyse des chapitres...")
    book_name = "Apprendre_LangChain"
    # `parse_chapters_smart` n'a jamais existe dans ce fichier : la seule
    # fonction d'analyse qu'il definit est `parse_chapters_langchain`, et elle
    # ne prend que le texte. Second `NameError` du meme script (C48, phase 0).
    chapters = parse_chapters_langchain(content)
    print(f"✅ {len(chapters)} chapitres détectés.")
    
    # Show chapter titles
    print("\n📚 Chapitres détectés:")
    for ch in chapters[:15]:  # Show first 15
        print(f"   {ch.number}. {ch.title[:70]}...")
    if len(chapters) > 15:
        print(f"   ... et {len(chapters) - 15} autres chapitres")
    
    # Create document with language="fr"
    doc = MarkdownDocument(
        book_name=book_name,
        language="fr",
        content=content,
        chapters=chapters,
        file_path=str(md_file)
    )
    
    # Save document
    dm = DocumentManager()
    print("\n💾 Sauvegarde du document...")
    dm.save_document(doc)
    
    # Copy images to output directory (if any)
    output_images_dir = settings.OUTPUT_DIR / book_name
    output_images_dir.mkdir(parents=True, exist_ok=True)
    
    print("📸 Recherche des images...")
    image_count = 0
    for ext in ['*.jpeg', '*.jpg', '*.png']:
        for img_file in source_dir.glob(ext):
            dest = output_images_dir / img_file.name
            if not dest.exists():
                shutil.copy2(img_file, dest)
            image_count += 1
    
    if image_count > 0:
        print(f"✅ {image_count} images copiées.")
    else:
        print("ℹ️  Aucune image trouvée.")
    
    print(f"\n🎉 Livre '{book_name}' importé avec succès!")
    print(f"📊 {len(chapters)} chapitres avec contenu en français")
    print("📱 Rafraîchissez votre navigateur pour voir le nouveau livre.")


if __name__ == "__main__":
    import_learning_langchain()
