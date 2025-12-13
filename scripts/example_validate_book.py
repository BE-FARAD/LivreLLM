#!/usr/bin/env python3
"""
Script pratique utilisant les hooks de validation
Valide un livre avant import dans la bibliothèque
"""

from pathlib import Path
import sys
import json

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.hooks.validators import validate_book_pipeline
from config.settings import settings


def validate_book_before_import(
    book_name: str,
    markdown_path: Path,
    json_dir: Path = None
) -> bool:
    """
    Valide un livre avant de l'importer dans la bibliothèque
    
    Args:
        book_name: Nom du livre (ex: "Le_Guide_Complet_LangGraph")
        markdown_path: Chemin vers le fichier .md source
        json_dir: Répertoire contenant le JSON (optionnel)
        
    Returns:
        True si toutes les validations passent, False sinon
    """
    print(f"\n{'='*80}")
    print(f" VALIDATION: {book_name} ".center(80, "="))
    print(f"{'='*80}\n")
    
    # Déterminer le chemin du JSON si un répertoire est fourni
    json_path = None
    if json_dir and json_dir.exists():
        json_path = json_dir / "json" / f"{book_name}.json"
        if not json_path.exists():
            json_path = json_dir / f"{book_name}.json"
        if not json_path.exists():
            print(f"⚠️  JSON non trouvé dans {json_dir}")
            json_path = None
    
    # Exécuter les validations
    results = validate_book_pipeline(
        book_name=book_name,
        markdown_path=markdown_path,
        json_path=json_path
    )
    
    # Afficher les résultats
    all_passed = True
    for check_name, result in results.items():
        icon = "✅" if result.passed else "❌"
        print(f"{icon} {check_name.upper()}: {result.message}")
        
        if not result.passed:
            all_passed = False
            # Afficher les détails en cas d'échec
            if result.details:
                print(f"   Détails: {json.dumps(result.details, indent=2, ensure_ascii=False)}")
    
    # Résumé
    print(f"\n{'─'*80}")
    total = len(results)
    passed = sum(1 for r in results.values() if r.passed)
    print(f"📊 Résultat: {passed}/{total} validations réussies")
    
    if all_passed:
        print("🎉 LE LIVRE EST PRÊT POUR L'IMPORT!")
    else:
        print("⚠️  LE LIVRE N'EST PAS PRÊT - Corrections nécessaires")
    
    print(f"{'='*80}\n")
    
    return all_passed


def main():
    """Fonction principale - exemples d'utilisation"""
    
    print("\n🔍 VALIDATION DES LIVRES FRANÇAIS")
    print("="*80)
    print()
    
    # Exemple 1: Le Guide Complet LangGraph
    print("## Exemple 1: Validation avec MD + JSON")
    validate_book_before_import(
        book_name="Le_Guide_Complet_LangGraph",
        markdown_path=settings.INPUT_DIR / "The Complete LangGraph Blueprint Build 50+ AI Agents for Business Success" / "Le Guide Complet LangGraph - Construire 50+ Agents IA.md",
        json_dir=settings.OUTPUT_DIR / "Le_Guide_Complet_LangGraph"
    )
    
    # Exemple 2: Apprendre LangChain
    print("\n## Exemple 2: Validation avec MD + JSON")
    validate_book_before_import(
        book_name="Apprendre_LangChain",
        markdown_path=settings.INPUT_DIR / "Learning LangChain Building" / "Apprendre LangChain - Construire des Applications IA et LLM.md",
        json_dir=settings.OUTPUT_DIR / "Apprendre_LangChain"
    )
    
    # Exemple 3: Transformateur de Courant
    print("\n## Exemple 3: Validation avec MD + JSON")
    transformateur_md = settings.INPUT_DIR / "Transformateur de courant" / "Transformateur de courant.md"
    
    if transformateur_md.exists():
        validate_book_before_import(
            book_name="Transformateur_de_Courant",
            markdown_path=transformateur_md,
            json_dir=settings.OUTPUT_DIR / "Transformateur_de_Courant"
        )
    else:
        # Essayer sans le sous-répertoire
        transformateur_md_alt = settings.INPUT_DIR / "Transformateur de courant.md"
        if transformateur_md_alt.exists():
            validate_book_before_import(
                book_name="Transformateur_de_Courant",
                markdown_path=transformateur_md_alt,
                json_dir=settings.OUTPUT_DIR / "Transformateur_de_Courant"
            )
        else:
            print(f"⚠️  Fichier 'Transformateur de courant.md' non trouvé")
    
    print("\n✨ Démonstration terminée!\n")


if __name__ == "__main__":
    main()
