#!/usr/bin/env python3
"""
Convertit le contenu des chapitres en paragraphes
et associe les fichiers audio existants
"""

from pathlib import Path
import sys
import json
import re

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config.settings import settings


def split_content_into_paragraphs(content: str):
    """Découpe le contenu en paragraphes"""
    # Supprimer les lignes vides multiples
    content = re.sub(r'\n\n+', '\n\n', content)
    
    # Séparer par double saut de ligne
    raw_paragraphs = content.split('\n\n')
    
    paragraphs = []
    para_num = 1
    
    for raw_para in raw_paragraphs:
        raw_para = raw_para.strip()
        
        # Ignorer les paragraphes vides ou trop courts
        if not raw_para or len(raw_para) < 10:
            continue
        
        # Ignorer les lignes de titres seules (headers markdown)
        if raw_para.startswith('#') and len(raw_para) < 100:
            # C'est un titre, on le garde quand même
            paragraphs.append({
                'number': para_num,
                'content': raw_para
            })
            para_num += 1
        # Ignorer les tableaux markdown
        elif '|' in raw_para and raw_para.count('|') > 4:
            # C'est un tableau, on le garde
            paragraphs.append({
                'number': para_num,
                'content': raw_para
            })
            para_num += 1
        else:
            # Paragraphe normal
            paragraphs.append({
                'number': para_num,
                'content': raw_para
            })
            para_num += 1
    
    return paragraphs


def find_existing_audio_for_para(book_name: str, chapter_num: int, para_num: int, audio_dir: Path):
    """Trouve le fichier audio existant pour un paragraphe"""
    pattern = f"{book_name}_ch{chapter_num:02d}_para{para_num:03d}_*.mp3"
    audio_files = list(audio_dir.glob(pattern))
    
    if audio_files:
        return audio_files[0].name
    return None


def process_book_json(json_path: Path):
    """Traite le JSON pour ajouter les paragraphes"""
    
    print(f"\n📋 Traitement du fichier: {json_path.name}\n")
    
    # Charger le JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        book_data = json.load(f)
    
    book_name = book_data.get('title', 'Unknown').replace(' ', '_')
    audio_dir = settings.AUDIO_DIR / book_name
    
    total_paragraphs = 0
    chapters_updated = 0
    
    # Traiter chaque chapitre
    for chapter in book_data['chapters']:
        chapter_num = chapter['number']
        chapter_title = chapter['title']
        content = chapter.get('content', '')
        
        print(f"  Ch{chapter_num}: {chapter_title}")
        
        if not content or len(content) < 50:
            print(f"      ⚠️  Contenu vide ou trop court ({len(content)} chars)\n")
            continue
        
        # Découper en paragraphes
        paragraphs = split_content_into_paragraphs(content)
        
        # Chercher les audios existants
        paragraphs_with_audio = []
        for para in paragraphs:
            para_num = para['number']
            audio_file = find_existing_audio_for_para(book_name, chapter_num, para_num, audio_dir)
            
            paragraphs_with_audio.append({
                'number': para_num,
                'content': para['content'],
                'audio_file': audio_file
            })
        
        # Mettre à jour le chapitre
        chapter['paragraphs'] = paragraphs_with_audio
        
        # Statistiques
        paras_with_audio = sum(1 for p in paragraphs_with_audio if p.get('audio_file'))
        print(f"      ✅ {len(paragraphs_with_audio)} paragraphes créés")
        print(f"      🎧 {paras_with_audio} paragraphes avec audio\n")
        
        total_paragraphs += len(paragraphs_with_audio)
        chapters_updated += 1
    
    # Sauvegarder
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(book_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ JSON mis à jour:")
    print(f"   - Chapitres traités: {chapters_updated}")
    print(f"   - Total paragraphes: {total_paragraphs}\n")
    
    return book_data


def main():
    """Processus principal"""
    
    print("\n" + "="*80)
    print(" CONVERSION CONTENU → PARAGRAPHES ".center(80, "="))
    print("="*80 + "\n")
    
    # Chemin du JSON
    json_path = settings.OUTPUT_DIR / "Transformateur_de_Courant" / "json" / "Transformateur_de_Courant.json"
    
    if not json_path.exists():
        print(f"❌ JSON non trouvé: {json_path}")
        return False
    
    # Traiter le JSON
    book_data = process_book_json(json_path)
    
    # Résumé final
    print("="*80)
    print("\n📊 RÉSUMÉ FINAL:")
    
    for chapter in book_data['chapters']:
        paras = len(chapter.get('paragraphs', []))
        with_audio = sum(1 for p in chapter.get('paragraphs', []) if p.get('audio_file'))
        print(f"   Ch{chapter['number']}: {paras} paragraphes ({with_audio} avec audio)")
    
    total_paras = sum(len(ch.get('paragraphs', [])) for ch in book_data['chapters'])
    total_audio = sum(sum(1 for p in ch.get('paragraphs', []) if p.get('audio_file')) for ch in book_data['chapters'])
    
    print(f"\n   TOTAL: {total_paras} paragraphes ({total_audio} avec audio)")
    
    print(f"\n💡 PROCHAINES ÉTAPES:")
    print(f"   1. Rafraîchir l'application web (F5)")
    print(f"   2. Vérifier que le texte s'affiche")
    print(f"   3. Générer les audios manquants si nécessaire")
    
    print(f"\n✅ Conversion terminée!\n")
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
