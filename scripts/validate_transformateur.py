#!/usr/bin/env python3
"""
Validation du livre: Transformateur de courant
"""

from pathlib import Path
import sys
import json

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from livrellm.hooks.validators import (
    FrenchMarkdownValidator,
    ChapterStructureValidator,
    AudioFileValidator,
    AudioAvailabilityValidator,
    validate_book_pipeline
)
from config.settings import settings


def main():
    """Validation complète du livre Transformateur de courant"""
    
    print("\n" + "="*80)
    print(" 🔍 VALIDATION: Transformateur de Courant ".center(80, "="))
    print("="*80 + "\n")
    
    # Chemins
    book_name = "Transformateur_de_Courant"
    md_path = settings.INPUT_DIR / "Transformateur de courant" / "Transformateur de courant.md"
    json_dir = settings.OUTPUT_DIR / "Transformateur_de_Courant"
    json_path = json_dir / "json" / f"{book_name}.json"
    
    print(f"📄 Fichier Markdown: {md_path}")
    print(f"   Existe: {'✅' if md_path.exists() else '❌'}")
    print(f"\n📋 Fichier JSON: {json_path}")
    print(f"   Existe: {'✅' if json_path.exists() else '❌'}")
    print(f"\n🎧 Répertoire Audio: data/audio/{book_name}")
    
    audio_dir = settings.AUDIO_DIR / book_name
    if audio_dir.exists():
        audio_files = list(audio_dir.glob("*.mp3"))
        print(f"   Fichiers audio: {len(audio_files)}")
    else:
        print("   Existe: ❌")
    
    print("\n" + "-"*80 + "\n")
    
    # Hook 1: Validation du français
    print("🇫🇷 HOOK 1: Validation du Markdown Français")
    print("-"*80)
    french_validator = FrenchMarkdownValidator(min_french_score=0.3)
    result = french_validator.validate(md_path)
    
    icon = "✅" if result.passed else "❌"
    print(f"{icon} {result.message}")
    if result.details:
        print(f"   Score français: {result.details.get('french_score', 0):.2%}")
        print(f"   Taille du fichier: {result.details.get('file_size', 0):,} caractères")
    
    print("\n" + "-"*80 + "\n")
    
    # Hook 2: Structure en chapitres
    print("📑 HOOK 2: Validation de la Structure en Chapitres")
    print("-"*80)
    structure_validator = ChapterStructureValidator(min_chapters=1)
    
    # Validation MD seul
    result_md = structure_validator.validate(md_path)
    icon = "✅" if result_md.passed else "❌"
    print(f"{icon} Markdown seul: {result_md.message}")
    if result_md.details:
        chapters = result_md.details.get('chapter_titles', [])
        print(f"   Chapitres détectés: {len(chapters)}")
        if chapters:
            for i, title in enumerate(chapters[:5], 1):
                print(f"   {i}. {title}")
            if len(chapters) > 5:
                print(f"   ... et {len(chapters) - 5} de plus")
    
    # Validation avec JSON si disponible
    if json_path.exists():
        result_json = structure_validator.validate(md_path, json_path)
        icon = "✅" if result_json.passed else "❌"
        print(f"\n{icon} Markdown + JSON: {result_json.message}")
        if result_json.details and not result_json.passed:
            print(f"   Détails: {json.dumps(result_json.details, indent=2, ensure_ascii=False)}")
    
    print("\n" + "-"*80 + "\n")
    
    # Hook 3: Fichiers audio
    print("🎧 HOOK 3: Validation des Fichiers Audio")
    print("-"*80)
    
    if json_path.exists():
        audio_validator = AudioFileValidator()
        result = audio_validator.validate(book_name, json_path)
        
        icon = "✅" if result.passed else "❌"
        print(f"{icon} {result.message}")
        
        if result.details:
            if result.passed:
                audio_files = result.details.get('audio_files', [])
                print("   Fichiers audio:")
                for audio in audio_files[:5]:
                    print(f"   - Ch{audio['chapter_number']}: {audio['audio_file']}")
                if len(audio_files) > 5:
                    print(f"   ... et {len(audio_files) - 5} de plus")
            else:
                missing = result.details.get('missing_audio', [])
                print("   Chapitres manquants:")
                for miss in missing[:5]:
                    print(f"   - Ch{miss['chapter_number']}: {miss['chapter_title']}")
    else:
        print("⚠️  JSON non trouvé - impossible de vérifier les audios")
    
    print("\n" + "-"*80 + "\n")
    
    # Hook 4: Disponibilité et intégrité
    print("✅ HOOK 4: Validation de la Disponibilité des Audios")
    print("-"*80)
    
    if json_path.exists():
        availability_validator = AudioAvailabilityValidator()
        result = availability_validator.validate(book_name, json_path)
        
        icon = "✅" if result.passed else "❌"
        print(f"{icon} {result.message}")
        
        if result.details:
            if result.passed:
                print(f"   Total chapitres: {result.details.get('total_chapters', 0)}")
                print(f"   Taille totale: {result.details.get('total_size_mb', 0)} MB")
                
                audio_files = result.details.get('audio_files', [])
                if audio_files:
                    print("\n   Détails des fichiers:")
                    for audio in audio_files[:5]:
                        size = audio.get('file_size_mb', 0)
                        print(f"   - Ch{audio['chapter_number']}: {audio['audio_file']} ({size} MB)")
                    if len(audio_files) > 5:
                        print(f"   ... et {len(audio_files) - 5} de plus")
            else:
                errors = result.details.get('validation_errors', [])
                print("\n   Erreurs de validation:")
                for err in errors[:5]:
                    print(f"   - Ch{err['chapter_number']}: {err['error']}")
    else:
        print("⚠️  JSON non trouvé - impossible de vérifier l'intégrité")
    
    print("\n" + "="*80)
    
    # Validation complète du pipeline
    print("\n📊 RÉSUMÉ DE LA VALIDATION COMPLÈTE")
    print("="*80 + "\n")
    
    results = validate_book_pipeline(
        book_name=book_name,
        markdown_path=md_path,
        json_path=json_path if json_path.exists() else None
    )
    
    total_checks = len(results)
    passed_checks = sum(1 for r in results.values() if r.passed)
    
    for check_name, result in results.items():
        icon = "✅" if result.passed else "❌"
        print(f"{icon} {check_name.upper()}: {result.message}")
    
    print(f"\n{'─'*80}")
    print(f"📊 Résultat Global: {passed_checks}/{total_checks} validations réussies")
    
    if passed_checks == total_checks:
        print("🎉 LE LIVRE EST PRÊT POUR LA BIBLIOTHÈQUE!")
    elif passed_checks >= total_checks * 0.75:
        print("⚠️  LE LIVRE EST PRESQUE PRÊT - Quelques ajustements recommandés")
    else:
        print("❌ LE LIVRE N'EST PAS PRÊT - Corrections nécessaires")
    
    print("="*80 + "\n")
    
    return passed_checks == total_checks


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
