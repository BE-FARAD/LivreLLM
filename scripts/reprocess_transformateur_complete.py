#!/usr/bin/env python3
"""
Redécoupage du livre Transformateur de Courant avec CONTENU COMPLET
"""

from pathlib import Path
import sys
import json
import re

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config.settings import settings


def extract_chapters_with_full_content(md_path: Path):
    """
    Extrait les chapitres avec leur contenu COMPLET
    """
    content = md_path.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    # Définir les points de départ de chaque chapitre
    chapter_definitions = [
        {"number": 0, "title": "Préambule et Introduction", "start_pattern": r'^# RECOMMANDATIONS'},
        {"number": 1, "title": "Chapitre 1: Glossaire et Définitions", "start_pattern": r'^#\s+1\.GLOSSAIRE'},
        {"number": 2, "title": "Chapitre 2: Généralités", "start_pattern": r'^#\s+2\.\s*GENERALITES'},
        {"number": 3, "title": "Chapitre 3: TC selon la norme CEI 44-1", "start_pattern": r'^#\s+2\.2\s+Transformateur'},
        {"number": 4, "title": "Chapitre 4: TC selon la norme ANSI/IEEE", "start_pattern": r'^#\s+2\.3\s+TC suivant la norme ANSI'},
        {"number": 5, "title": "Chapitre 5: TC selon la norme BS 3938", "start_pattern": r'^#\s+2\.4\s+TC suivant la norme BS'},
        {"number": 6, "title": "Chapitre 6: TC selon la norme CEI 44-6", "start_pattern": r'^#\s+2\.5\s+TC suivant la norme CEI 44-6'},
    ]
    
    # Trouver les lignes de départ de chaque chapitre
    chapter_starts = []
    for ch_def in chapter_definitions:
        for i, line in enumerate(lines):
            if re.search(ch_def['start_pattern'], line, re.IGNORECASE):
                chapter_starts.append({
                    'number': ch_def['number'],
                    'title': ch_def['title'],
                    'start_line': i
                })
                break
    
    # Trier  par ligne de départ
    chapter_starts.sort(key=lambda x: x['start_line'])
    
    # Extraire le contenu de chaque chapitre
    chapters = []
    for i, ch_start in enumerate(chapter_starts):
        start_line = ch_start['start_line']
        
        # Trouver la ligne de fin (début du chapitre suivant ou fin du fichier)
        if i + 1 < len(chapter_starts):
            end_line = chapter_starts[i + 1]['start_line']
        else:
            end_line = len(lines)
        
        # Extraire le contenu
        chapter_lines = lines[start_line:end_line]
        chapter_content = '\n'.join(chapter_lines).strip()
        
        chapters.append({
            'number': ch_start['number'],
            'title': ch_start['title'],
            'content': chapter_content,
            'start_line': start_line,
            'end_line': end_line,
            'line_count': end_line - start_line
        })
    
    return chapters


def update_json_with_chapters(json_path: Path, chapters: list):
    """Met à jour le JSON avec les chapitres contenant le contenu complet"""
    
    # Charger le JSON existant ou créer un nouveau
    if json_path.exists():
        with open(json_path, 'r', encoding='utf-8') as f:
            book_data = json.load(f)
    else:
        book_data = {
            'title': 'Transformateur de Courant',
            'language': 'fr',
            'chapters': []
        }
    
    # Mettre à jour les chapitres
    book_data['chapters'] = []
    for ch in chapters:
        book_data['chapters'].append({
            'number': ch['number'],
            'title': ch['title'],
            'content': ch['content'],  # CONTENU COMPLET !
            'paragraphs': []  # À remplir par le processus d'import
        })
    
    # Sauvegarder
    json_path.parent.mkdir(parents=True, exist_ok=True)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(book_data, f, ensure_ascii=False, indent=2)
    
    return book_data


def main():
    """Processus complet de redécoupage avec contenu"""
    
    print("\n" + "="*80)
    print(" REDÉCOUPAGE AVEC CONTENU COMPLET: Transformateur de Courant ".center(80, "="))
    print("="*80 + "\n")
    
    # Chemins
    md_path = settings.INPUT_DIR / "Transformateur de courant" / "Transformateur de courant.md"
    json_path = settings.OUTPUT_DIR / "Transformateur_de_Courant" / "json" / "Transformateur_de_Courant.json"
    
    if not md_path.exists():
        print(f"❌ Fichier non trouvé: {md_path}")
        return False
    
    print(f"📄 Lecture du document: {md_path.name}")
    print(f"   Taille: {md_path.stat().st_size:,} bytes\n")
    
    # Étape 1: Extraire les chapitres avec leur contenu COMPLET
    print("🔍 Étape 1: Extraction des chapitres avec contenu complet...")
    chapters = extract_chapters_with_full_content(md_path)
    print(f"   ✅ {len(chapters)} chapitres extraits\n")
    
    # Afficher un résumé
    print("📚 Chapitres identifiés:\n")
    for ch in chapters:
        content_size = len(ch['content'])
        print(f"   Ch{ch['number']}: {ch['title']}")
        print(f"      Lignes: {ch['start_line']}-{ch['end_line']} ({ch['line_count']} lignes)")
        print(f"      Contenu: {content_size:,} caractères\n")
    
    # Étape 2: Mettre à jour le JSON
    print("📋 Étape 2: Mise à jour du JSON avec le contenu complet...")
    book_data = update_json_with_chapters(json_path, chapters)
    print(f"   ✅ JSON mis à jour: {json_path}\n")
    
    # Vérification
    print("✅ Étape 3: Vérification...")
    total_content = sum(len(ch['content']) for ch in book_data['chapters'])
    print(f"   - Chapitres dans le JSON: {len(book_data['chapters'])}")
    print(f"   - Contenu total: {total_content:,} caractères")
    print(f"   - Moyenne par chapitre: {total_content // len(book_data['chapters']):,} caractères\n")
    
    # Résumé
    print("="*80)
    print("\n📊 RÉSUMÉ:")
    print(f"   ✅ {len(chapters)} chapitres extraits avec contenu complet")
    print(f"   ✅ JSON mis à jour: {json_path.name}")
    print(f"   ✅ Contenu total: {total_content:,} caractères")
    
    print("\n💡 PROCHAINES ÉTAPES:")
    print("   1. Relancer la validation: python scripts/validate_transformateur.py")
    print("   2. Générer les audios: python scripts/generate_all_audios.py")
    print("\n✅ Redécoupage terminé!\n")
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
