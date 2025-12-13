#!/usr/bin/env python3
"""
Script de test des hooks de validation
Démontre l'utilisation des 4 hooks pour valider les livres français
"""

from pathlib import Path
import sys

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.hooks.validators import (
    FrenchMarkdownValidator,
    ChapterStructureValidator,
    AudioFileValidator,
    AudioAvailabilityValidator,
    validate_book_pipeline
)
from config.settings import settings


def test_individual_hooks():
    """Test de chaque hook individuellement"""
    
    print("=" * 80)
    print(" TEST DES HOOKS INDIVIDUELS ".center(80, "="))
    print("=" * 80)
    print()
    
    # Chemins de test
    langgraph_md = settings.INPUT_DIR / "The Complete LangGraph Blueprint Build 50+ AI Agents for Business Success" / "Le Guide Complet LangGraph - Construire 50+ Agents IA.md"
    langgraph_json = settings.OUTPUT_DIR / "Le_Guide_Complet_LangGraph.json"
    
    langchain_md = settings.INPUT_DIR / "Learning LangChain Building" / "Apprendre LangChain - Construire des Applications IA et LLM.md"
    langchain_json = settings.OUTPUT_DIR / "Apprendre_LangChain.json"
    
    transformateur_md = settings.INPUT_DIR / "Transformateur de courant.md"
    transformateur_json = settings.OUTPUT_DIR / "Transformateur_de_Courant.json"
    
    # Hook 1: Validation du markdown français
    print("🔍 HOOK 1: Validation du Markdown Français")
    print("-" * 80)
    
    french_validator = FrenchMarkdownValidator(min_french_score=0.3)
    
    for name, md_path in [
        ("Le Guide Complet LangGraph", langgraph_md),
        ("Apprendre LangChain", langchain_md),
        ("Transformateur de Courant", transformateur_md)
    ]:
        result = french_validator.validate(md_path)
        print(f"\n📖 {name}:")
        print(f"   {result}")
        if result.details:
            print(f"   Score français: {result.details.get('french_score', 0):.2%}")
    
    print("\n" + "=" * 80)
    
    # Hook 2: Validation de la structure en chapitres
    print("\n🔍 HOOK 2: Validation de la Structure en Chapitres")
    print("-" * 80)
    
    structure_validator = ChapterStructureValidator(min_chapters=1)
    
    test_cases = [
        ("Le Guide Complet LangGraph", langgraph_md, langgraph_json),
        ("Apprendre LangChain", langchain_md, langchain_json),
        ("Transformateur de Courant", transformateur_md, transformateur_json)
    ]
    
    for name, md_path, json_path in test_cases:
        # Test avec markdown seul
        result_md = structure_validator.validate(md_path)
        print(f"\n📖 {name} (Markdown seulement):")
        print(f"   {result_md}")
        if result_md.details:
            print(f"   Chapitres détectés: {result_md.details.get('chapters_count', 0)}")
        
        # Test avec JSON si disponible
        if json_path.exists():
            result_json = structure_validator.validate(md_path, json_path)
            print(f"\n📖 {name} (Markdown + JSON):")
            print(f"   {result_json}")
    
    print("\n" + "=" * 80)
    
    # Hook 3: Validation des fichiers audio
    print("\n🔍 HOOK 3: Validation des Fichiers Audio")
    print("-" * 80)
    
    audio_validator = AudioFileValidator()
    
    audio_test_cases = [
        ("Le_Guide_Complet_LangGraph", langgraph_json),
        ("Apprendre_LangChain", langchain_json),
        ("Transformateur_de_Courant", transformateur_json)
    ]
    
    for book_name, json_path in audio_test_cases:
        if json_path.exists():
            result = audio_validator.validate(book_name, json_path)
            print(f"\n🎧 {book_name}:")
            print(f"   {result}")
            if result.details and result.passed:
                print(f"   Total chapitres: {result.details.get('total_chapters', 0)}")
        else:
            print(f"\n🎧 {book_name}:")
            print(f"   ⚠️  JSON non trouvé: {json_path}")
    
    print("\n" + "=" * 80)
    
    # Hook 4: Validation de la disponibilité des audios
    print("\n🔍 HOOK 4: Validation de la Disponibilité des Audios")
    print("-" * 80)
    
    availability_validator = AudioAvailabilityValidator()
    
    for book_name, json_path in audio_test_cases:
        if json_path.exists():
            result = availability_validator.validate(book_name, json_path)
            print(f"\n🎧 {book_name}:")
            print(f"   {result}")
            if result.details and result.passed:
                print(f"   Total chapitres: {result.details.get('total_chapters', 0)}")
                print(f"   Taille totale: {result.details.get('total_size_mb', 0)} MB")
        else:
            print(f"\n🎧 {book_name}:")
            print(f"   ⚠️  JSON non trouvé: {json_path}")
    
    print("\n" + "=" * 80)
    print()


def test_pipeline_validation():
    """Test de la validation complète du pipeline"""
    
    print("=" * 80)
    print(" TEST DU PIPELINE COMPLET ".center(80, "="))
    print("=" * 80)
    print()
    
    books = [
        {
            'name': 'Le_Guide_Complet_LangGraph',
            'markdown': settings.INPUT_DIR / "The Complete LangGraph Blueprint Build 50+ AI Agents for Business Success" / "Le Guide Complet LangGraph - Construire 50+ Agents IA.md",
            'json': settings.OUTPUT_DIR / "Le_Guide_Complet_LangGraph.json"
        },
        {
            'name': 'Apprendre_LangChain',
            'markdown': settings.INPUT_DIR / "Learning LangChain Building" / "Apprendre LangChain - Construire des Applications IA et LLM.md",
            'json': settings.OUTPUT_DIR / "Apprendre_LangChain.json"
        },
        {
            'name': 'Transformateur_de_Courant',
            'markdown': settings.INPUT_DIR / "Transformateur de courant.md",
            'json': settings.OUTPUT_DIR / "Transformateur_de_Courant.json"
        }
    ]
    
    for book in books:
        print(f"\n{'=' * 80}")
        print(f" 📚 {book['name']} ".center(80, "="))
        print(f"{'=' * 80}\n")
        
        results = validate_book_pipeline(
            book_name=book['name'],
            markdown_path=book['markdown'],
            json_path=book['json'] if book['json'].exists() else None
        )
        
        for check_name, result in results.items():
            icon = "✅" if result.passed else "❌"
            print(f"{icon} {check_name.upper()}: {result.message}")
        
        # Résumé
        total_checks = len(results)
        passed_checks = sum(1 for r in results.values() if r.passed)
        
        print(f"\n📊 Résumé: {passed_checks}/{total_checks} validations réussies")
        
        if passed_checks == total_checks:
            print("🎉 Tous les checks sont passés !")
        else:
            print("⚠️  Certains checks ont échoué")
    
    print("\n" + "=" * 80)
    print()


def main():
    """Fonction principale"""
    print("\n")
    print("🚀 SYSTÈME DE VALIDATION DES LIVRES FRANÇAIS")
    print("=" * 80)
    print()
    print("Ce script teste les 4 hooks de validation:")
    print("  1. 🇫🇷 Validation du markdown français")
    print("  2. 📑 Validation de la structure en chapitres")
    print("  3. 🎧 Validation de la présence des fichiers audio")
    print("  4. ✅ Validation de la disponibilité et intégrité des audios")
    print()
    
    # Test des hooks individuels
    test_individual_hooks()
    
    # Test du pipeline complet
    test_pipeline_validation()
    
    print("\n✨ Tests terminés !\n")


if __name__ == "__main__":
    main()
