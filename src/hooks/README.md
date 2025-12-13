# 🔍 Système de Validation des Livres (Hooks)

Ce module fournit un système complet de validation pour garantir la qualité et l'intégrité des livres importés dans LivreLLM.

## 📋 Les 4 Hooks de Validation

### 🇫🇷 Hook 1: Validation du Markdown Français
**Classe**: `FrenchMarkdownValidator`

Vérifie qu'un fichier markdown est bien en français avant l'import.

**Critères de validation:**
- Présence de caractères français (accents: à, é, è, etc.)
- Mots-clés français communs (chapitre, le, la, les, etc.)
- Pattern "Chapitre X"
- Élisions françaises (qu', l', d', etc.)

**Usage:**
```python
from src.hooks.validators import FrenchMarkdownValidator

validator = FrenchMarkdownValidator(min_french_score=0.3)
result = validator.validate(Path("mon_livre.md"))

if result.passed:
    print(f"✅ Livre français: {result.details['french_score']:.2%}")
else:
    print(f"❌ Pas français: {result.message}")
```

### 📑 Hook 2: Validation de la Structure en Chapitres
**Classe**: `ChapterStructureValidator`

Vérifie que le livre est correctement structuré en chapitres et que les titres correspondent entre le markdown et le JSON traité.

**Critères de validation:**
- Détection de chapitres via patterns regex
- Nombre minimal de chapitres (configurable)
- Correspondance des titres MD ↔ JSON
- Numérotation cohérente

**Patterns supportés:**
```markdown
# Chapitre 1: Titre
## Chapitre 2: Titre
# <span></span>Chapitre 3: Titre
# **Chapitre 4**: Titre
```

**Usage:**
```python
from src.hooks.validators import ChapterStructureValidator

validator = ChapterStructureValidator(min_chapters=1)

# Validation MD seul
result = validator.validate(markdown_path=Path("livre.md"))

# Validation MD + JSON
result = validator.validate(
    markdown_path=Path("livre.md"),
    json_path=Path("livre.json")
)
```

### 🎧 Hook 3: Validation des Fichiers Audio
**Classe**: `AudioFileValidator`

Vérifie que chaque chapitre possède son fichier audio associé.

**Critères de validation:**
- Présence du répertoire audio du livre
- Fichier audio pour chaque chapitre
- Pattern de nommage: `BookName_chXX_FULL_*.mp3`

**Usage:**
```python
from src.hooks.validators import AudioFileValidator

validator = AudioFileValidator()
result = validator.validate(
    book_name="Mon_Livre",
    json_path=Path("Mon_Livre.json")
)

if result.passed:
    print(f"✅ {result.details['total_chapters']} audios trouvés")
else:
    missing = result.details['missing_audio']
    print(f"❌ Chapitres sans audio: {missing}")
```

### ✅ Hook 4: Validation de la Disponibilité des Audios
**Classe**: `AudioAvailabilityValidator`

Validation approfondie de l'intégrité des fichiers audio.

**Critères de validation:**
- Existence des fichiers
- Taille minimale (1 KB)
- Fichier réellement accessible
- Calcul de la taille totale

**Usage:**
```python
from src.hooks.validators import AudioAvailabilityValidator

validator = AudioAvailabilityValidator()
result = validator.validate(
    book_name="Mon_Livre",
    json_path=Path("Mon_Livre.json")
)

if result.passed:
    total_mb = result.details['total_size_mb']
    print(f"✅ Audios valides: {total_mb} MB")
```

## 🚀 Validation Complète du Pipeline

La fonction `validate_book_pipeline()` exécute tous les hooks en une seule fois.

**Usage:**
```python
from pathlib import Path
from src.hooks.validators import validate_book_pipeline

results = validate_book_pipeline(
    book_name="Mon_Livre",
    markdown_path=Path("mon_livre.md"),
    json_path=Path("mon_livre.json"),
    skip_checks=[]  # Optionnel: ['french', 'structure', 'audio', 'availability']
)

# Vérifier les résultats
for check_name, result in results.items():
    if result.passed:
        print(f"✅ {check_name.upper()}: {result.message}")
    else:
        print(f"❌ {check_name.upper()}: {result.message}")

# Vérifier si tout est OK
all_passed = all(r.passed for r in results.values())
```

## 📝 Scripts d'Exemple

### Test Complet
```bash
python scripts/test_validation_hooks.py
```
Ce script teste chaque hook individuellement et le pipeline complet sur tous les livres français.

### Validation Pratique
```bash
python scripts/example_validate_book.py
```
Démontre l'utilisation pratique pour valider un livre avant import.

## 🎯 Cas d'Usage

### 1. Avant l'Import d'un Nouveau Livre
```python
from src.hooks.validators import validate_book_pipeline

# Valider le markdown avant traitement
results = validate_book_pipeline(
    book_name="Nouveau_Livre",
    markdown_path=Path("nouveau_livre.md"),
    skip_checks=['audio', 'availability']  # Pas encore d'audio
)

if results['french'].passed and results['structure'].passed:
    print("✅ Prêt pour le traitement")
    # Lancer le traitement...
```

### 2. Après Génération des Audios
```python
# Valider que tous les audios sont bien générés
results = validate_book_pipeline(
    book_name="Nouveau_Livre",
    markdown_path=Path("nouveau_livre.md"),
    json_path=Path("nouveau_livre.json")
)

if all(r.passed for r in results.values()):
    print("✅ Livre complet et prêt pour la bibliothèque")
```

### 3. Vérification de l'Intégrité de la Bibliothèque
```python
from pathlib import Path
from src.hooks.validators import AudioAvailabilityValidator

validator = AudioAvailabilityValidator()

for book_json in Path("data/02-output").rglob("*.json"):
    book_name = book_json.stem
    result = validator.validate(book_name, book_json)
    
    if not result.passed:
        print(f"⚠️  {book_name}: {result.message}")
```

## 🔧 Configuration

### Ajuster les Critères de Validation

```python
# Markdown français plus strict
french_validator = FrenchMarkdownValidator(min_french_score=0.5)

# Livres avec plus de chapitres
structure_validator = ChapterStructureValidator(min_chapters=5)

# Audio dans un autre répertoire
audio_validator = AudioFileValidator(audio_dir=Path("/custom/audio"))
```

### Patterns de Chapitres Personnalisés

Pour ajouter un nouveau pattern de détection de chapitre:

```python
from src.hooks.validators import ChapterStructureValidator

validator = ChapterStructureValidator()

# Ajouter un pattern personnalisé
validator.CHAPTER_PATTERNS.append(
    r'^#\s+Mon_Pattern_Chapitre\s+(\d+)'
)
```

## 📊 Structure de `ValidationResult`

Chaque validation retourne un objet `ValidationResult`:

```python
@dataclass
class ValidationResult:
    passed: bool          # True si la validation passe
    message: str          # Message descriptif
    details: Optional[Dict]  # Détails additionnels (optionnel)
```

**Exemple de details:**
```python
{
    'french_score': 0.95,
    'chapters_count': 12,
    'total_size_mb': 156.7,
    'validation_errors': [...],
    'audio_files': [...]
}
```

## ⚡ Exemples Complets

### Script de Validation Batch
```python
#!/usr/bin/env python3
"""Valider tous les livres de la bibliothèque"""
from pathlib import Path
from src.hooks.validators import validate_book_pipeline
from config.settings import settings

def validate_all_books():
    """Valide tous les livres"""
    books_dir = settings.OUTPUT_DIR
    
    for book_dir in books_dir.iterdir():
        if not book_dir.is_dir():
            continue
            
        json_file = book_dir / "json" / f"{book_dir.name}.json"
        if not json_file.exists():
            continue
        
        # Trouver le markdown source
        md_file = settings.INPUT_DIR / f"{book_dir.name}.md"
        
        if md_file.exists():
            results = validate_book_pipeline(
                book_name=book_dir.name,
                markdown_path=md_file,
                json_path=json_file
            )
            
            all_passed = all(r.passed for r in results.values())
            status = "✅" if all_passed else "❌"
            print(f"{status} {book_dir.name}")

if __name__ == "__main__":
    validate_all_books()
```

## 🛠️ Développement

### Ajouter un Nouveau Hook

1. Créer une nouvelle classe dans `src/hooks/validators.py`:
```python
class MonNouveauValidator:
    """Description du validateur"""
    
    def validate(self, *args, **kwargs) -> ValidationResult:
        # Logique de validation
        return ValidationResult(
            passed=True,
            message="Validation OK",
            details={}
        )
```

2. L'ajouter à `validate_book_pipeline()`:
```python
def validate_book_pipeline(...):
    # ...
    if 'mon_check' not in skip_checks:
        validator = MonNouveauValidator()
        results['mon_check'] = validator.validate(...)
```

3. Mettre à jour `__init__.py`:
```python
from .validators import MonNouveauValidator

__all__ = [..., 'MonNouveauValidator']
```

## 📦 Intégration

### Dans un Script d'Import
```python
from src.hooks.validators import validate_book_pipeline

def import_book(md_path):
    # 1. Valider le markdown
    results = validate_book_pipeline(
        book_name=md_path.stem,
        markdown_path=md_path,
        skip_checks=['audio', 'availability']
    )
    
    if not results['french'].passed:
        raise ValueError("Le livre n'est pas en français")
    
    if not results['structure'].passed:
        raise ValueError("Structure de chapitres invalide")
    
    # 2. Traiter le livre
    # ...
    
    # 3. Générer les audios
    # ...
    
    # 4. Validation finale
    final_results = validate_book_pipeline(
        book_name=book_name,
        markdown_path=md_path,
        json_path=json_path
    )
    
    if not all(r.passed for r in final_results.values()):
        raise ValueError("Validation finale échouée")
```

## 🎓 Bonnes Pratiques

1. **Valider tôt**: Vérifier le markdown français AVANT tout traitement
2. **Valider souvent**: Après chaque étape (parsing, audio, etc.)
3. **Logger les détails**: Utiliser `result.details` pour le debugging
4. **Gestion d'erreurs**: Ne pas ignorer les échecs de validation
5. **Tests réguliers**: Valider périodiquement toute la bibliothèque

## 📚 Documentation API Complète

Voir la docstring de chaque classe pour la documentation complète:
```python
help(FrenchMarkdownValidator)
help(ChapterStructureValidator)
help(AudioFileValidator)
help(AudioAvailabilityValidator)
```

---

**Créé pour LivreLLM** - Système de validation des livres français 🇫🇷📚
