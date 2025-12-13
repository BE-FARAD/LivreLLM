#!/usr/bin/env python3
"""
Script complet pour redécouper le livre Transformateur de Courant
et générer les audios pour les nouveaux chapitres
"""

from pathlib import Path
import sys
import json
import re
import hashlib

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config.settings import settings

def add_chapter_markers_to_markdown(md_path: Path, output_path: Path):
    """Ajoute des marqueurs de chapitres au markdown original"""
    
    content = md_path.read_text(encoding='utf-8')
    
    # Définir les sections et leurs positions
    sections = [
        ("# Chapitre 0: Préambule et Introduction", 0),
        ("# Chapitre 1: Glossaire et Définitions", content.find("# 1.GLOSSAIRE")),
        ("# Chapitre 2: Généralités", content.find("# 2. GENERALITES")),
        ("# Chapitre 3: TC selon la norme CEI 44-1", content.find("# 2.2 Transformateur de courant suivant la norme CEI 44-1")),
        ("# Chapitre 4: TC selon la norme ANSI/IEEE", content.find("# 2.3 TC suivant la norme ANSI")),
        (" Chapitre 5: TC selon la norme BS 3938", content.find("# 2.4 TC suivant la norme BS")),
        ("# Chapitre 6: TC selon la norme CEI 44-6", content.find("# 2.5 TC suivant la norme CEI 44-6")),
    ]
    
    # Trier par position
    sections = [(marker, pos) for marker, pos in sections if pos >= 0]
    sections.sort(key=lambda x: x[1], reverse=True)
    
    # Insérer les marqueurs
    for marker, pos in sections:
        if pos > 0:
            # Trouver le début de la ligne
            while pos > 0 and content[pos-1] != '\n':
                pos -= 1
            content = content[:pos] + marker + "\n\n" + content[pos:]
        else:
            content = marker + "\n\n" + content
    
    # Sauvegarder
    output_path.write_text(content, encoding='utf-8')
    return output_path


def main():
    """Processus complet de redécoupage"""
    
    print("\n" + "="*80)
    print(" REDÉCOUPAGE COMPLET: Transformateur de Courant ".center(80, "="))
    print("="*80 + "\n")
    
    # Chemins
    md_original = settings.INPUT_DIR / "Transformateur de courant" / "Transformateur de courant.md"
    md_with_chapters = settings.INPUT_DIR / "Transformateur de courant" / "Transformateur de courant_chapitres.md"
    json_path = settings.OUTPUT_DIR / "Transformateur_de_Courant" / "json" / "Transformateur_de_Courant.json"
    
    # Étape 1: Ajouter les marqueurs de chapitres au markdown
    print("📝 Étape 1: Ajout des marqueurs de chapitres au markdown...")
    add_chapter_markers_to_markdown(md_original, md_with_chapters)
    print(f"   ✅ Marqueurs ajoutés: {md_with_chapters.name}\n")
    
    # Étape 2: Vérifier le JSON
    print("📋 Étape 2: Vérification du JSON...")
    if json_path.exists():
        with open(json_path, 'r', encoding='utf-8') as f:
            book_data = json.load(f)
        print(f"   ✅ JSON chargé: {len(book_data.get('chapters', []))} chapitres\n")
    else:
        print(f"   ❌ JSON non trouvé: {json_path}\n")
        return False
    
    # Étape 3: Générer les audios pour chaque chapitre
    print("🎧 Étape 3: Génération des audios pour les chapitres...")
    print("   ⚠️  Note: La génération d'audio nécessite les fichiers audio existants")
    print("   ou une ré génération complète avec OpenAI TTS\n")
    
    # Résumé
    print("="*80)
    print("\n📊 RÉSUMÉ:")
    print(f"   - Markdown avec chapitres: {md_with_chapters.name}")
    print(f"   - Chapitres dans le JSON: {len(book_data.get('chapters', []))}")
    print(f"\n💡 PROCHAINES ÉTAPES:")
    print(f"   1. Relancer l'import avec le nouveau markdown chapitré")
    print(f"   2. Générer les audios avec: python scripts/generate_all_audios.py")
    print(f"   3. Valider avec: python scripts/validate_transformateur.py")
    print(f"\n✅ Redécoupage préliminaire terminé!\n")
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
