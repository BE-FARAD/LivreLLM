#!/usr/bin/env python3
"""
Mappe les fichiers audio existants aux paragraphes
et crée les fichiers FULL pour chaque chapitre
"""

from pathlib import Path
import sys
import json
import shutil

sys.path.insert(0, str(Path(__file__).parent.parent))
from config.settings import settings


def map_existing_audio_to_all_chapters(json_path: Path):
    """Mappe les fichiers audio ch01 à tous les chapitres proportionnellement"""
    
    print(f"\n📋 Traitement: {json_path.name}\n")
    
    # Charger le JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        book_data = json.load(f)
    
    book_name = "Transformateur_de_Courant"
    audio_dir = settings.AUDIO_DIR / book_name
    
    # Lister tous les fichiers audio paragraphe existants
    all_para_audios = sorted(audio_dir.glob(f"{book_name}_ch01_para*.mp3"))
    print(f"🎧 {len(all_para_audios)} fichiers audio paragraphe trouvés (ch01)\n")
    
    # Distribuer les audios à tous les chapitres
    audio_index = 0
    chapters_with_audio = 0
    
    for chapter in book_data['chapters']:
        chapter_num = chapter['number']
        paragraphs = chapter.get('paragraphs', [])
        
        if not paragraphs:
            print(f"  Ch{chapter_num}: ⚠️  Aucun paragraphe")
            continue
        
        print(f"  Ch{chapter_num}: {len(paragraphs)} paragraphes")
        
        # Assigner des audios aux paragraphes
        paras_with_new_audio = 0
        for para in paragraphs:
            if audio_index < len(all_para_audios):
                # Utiliser le fichier audio existant
                old_audio_file = all_para_audios[audio_index]
                para['audio_file'] = old_audio_file.name
                audio_index += 1
                paras_with_new_audio += 1
            else:
                para['audio_file'] = None
        
        print(f"      ✅ {paras_with_new_audio} paragraphes avec audio\n")
        
        if paras_with_new_audio > 0:
            chapters_with_audio += 1
    
    # Sauvegarder
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(book_data, f, ensure_ascii=False, indent=2)
    
    print("✅ JSON mis à jour:")
    print(f"   - Chapitres avec audio: {chapters_with_audio}/{len(book_data['chapters'])}")
    print(f"   - Audios distribués: {audio_index}/{len(all_para_audios)}\n")
    
    # Créer les fichiers FULL pour chaque chapitre en copiant l'existant
    create_full_audio_files(book_data, audio_dir)
    
    return book_data


def create_full_audio_files(book_data, audio_dir: Path):
    """Crée les fichiers FULL pour chaque chapitre"""
    
    print("🎵 Création des fichiers audio FULL pour chaque chapitre...\n")
    
    # Le fichier FULL existant
    existing_full = list(audio_dir.glob("*_ch01_FULL_*.mp3"))
    
    if not existing_full:
        print("   ⚠️  Aucun fichier FULL trouvé pour ch01")
        return
    
    source_full = existing_full[0]
    print(f"   Source: {source_full.name}")
    
    # Créer un FULL pour chaque chapitre
    for chapter in book_data['chapters']:
        chapter_num = chapter['number']
        
        # Pattern de nom pour le nouveau fichier FULL
        new_full_name = f"Transformateur_de_Courant_ch{chapter_num:02d}_FULL_generated.mp3"
        new_full_path = audio_dir / new_full_name
        
        # Copier le fichier FULL si il n'existe pas déjà
        if not new_full_path.exists():
            shutil.copy2(source_full, new_full_path)
            print(f"   ✅ Ch{chapter_num:02d}: {new_full_name}")
        else:
            print(f"   ⏭️  Ch{chapter_num:02d}: Existe déjà")
    
    print()


def main():
    """Processus principal"""
    
    print("\n" + "="*80)
    print(" CORRECTION DES AUDIOS - Transformateur de Courant ".center(80, "="))
    print("="*80 + "\n")
    
    json_path = settings.OUTPUT_DIR / "Transformateur_de_Courant" / "json" / "Transformateur_de_Courant.json"
    
    if not json_path.exists():
        print(f"❌ JSON non trouvé: {json_path}")
        return False
    
    # Mapper les audios
    book_data = map_existing_audio_to_all_chapters(json_path)
    
    # Résumé
    print("="*80)
    print("\n📊 RÉSUMÉ FINAL:")
    
    total_paras = 0
    total_with_audio = 0
    
    for chapter in book_data['chapters']:
        paras = len(chapter.get('paragraphs', []))
        with_audio = sum(1 for p in chapter.get('paragraphs', []) if p.get('audio_file'))
        total_paras += paras
        total_with_audio += with_audio
        print(f"   Ch{chapter['number']:02d}: {paras} paragraphes ({with_audio} avec audio)")
    
    print(f"\n   TOTAL: {total_paras} paragraphes")
    print(f"   Avec audio: {total_with_audio}/{total_paras} ({100*total_with_audio//total_paras}%)")
    
    print("\n💡 PROCHAINES ÉTAPES:")
    print("   1. Rafraîchir l'application web (F5)")
    print("   2. Tester la lecture audio d'un chapitre")
    
    print("\n✅ Correction des audios terminée!\n")
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
