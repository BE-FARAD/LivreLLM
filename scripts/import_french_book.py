import sys
from pathlib import Path
import shutil

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from livrellm.conversion.marker_converter import MarkerConverter
from livrellm.conversion.markdown_document import MarkdownDocument
from livrellm.translation.document_manager import DocumentManager
from config.settings import settings

def import_french_book():
    """Import the French version of LangGraph book."""
    
    # Source files
    source_dir = settings.INPUT_DIR / "The Complete LangGraph Blueprint Build 50+ AI Agents for Business Success"
    md_file = source_dir / "Le Guide Complet LangGraph - Construire 50+ Agents IA.md"
    
    if not md_file.exists():
        print(f"❌ Fichier markdown français introuvable: {md_file}")
        return
    
    print(f"📄 Lecture de {md_file.name}...")
    content = md_file.read_text(encoding="utf-8")
    
    # Parse with marker converter
    converter = MarkerConverter()
    
    print("🧠 Analyse des chapitres...")
    chapters = converter._parse_chapters(content)
    print(f"✅ {len(chapters)} chapitres détectés.")
    
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
    print("💾 Sauvegarde du document...")
    dm.save_document(doc)
    
    # Copy images to output directory
    output_images_dir = settings.OUTPUT_DIR / book_name
    output_images_dir.mkdir(parents=True, exist_ok=True)
    
    print("📸 Copie des images...")
    image_count = 0
    for img_file in source_dir.glob("*.jpeg"):
        dest = output_images_dir / img_file.name
        shutil.copy2(img_file, dest)
        image_count += 1
    
    print(f"✅ {image_count} images copiées.")
    print(f"🎉 Livre '{book_name}' importé avec succès!")
    print("📱 Rafraîchissez Streamlit pour voir le nouveau livre.")

if __name__ == "__main__":
    import_french_book()
