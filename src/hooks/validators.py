"""
Validators for validating book processing pipeline.
Each validator checks a specific aspect of the book processing.
"""

import re
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
import json

from config.settings import settings


@dataclass
class ValidationResult:
    """Result of a validation check"""
    passed: bool
    message: str
    details: Optional[Dict] = None
    
    def __str__(self):
        status = "✅ PASS" if self.passed else "❌ FAIL"
        return f"{status}: {self.message}"


class FrenchMarkdownValidator:
    """
    Hook 1: Valide que le fichier markdown est en français
    Récupère uniquement les fichiers markdown français avant le téléchargement dans la bibliothèque
    """
    
    # Mots-clés français communs
    FRENCH_KEYWORDS = [
        'chapitre', 'le', 'la', 'les', 'un', 'une', 'des', 'de', 'du',
        'et', 'ou', 'avec', 'pour', 'dans', 'sur', 'par', 'est', 'sont',
        'être', 'avoir', 'faire', 'à', 'au', 'aux', 'ce', 'cette', 'ces'
    ]
    
    # Patterns pour détecter le contenu français
    FRENCH_PATTERNS = [
        r'[àâäéèêëïîôùûüÿç]',  # Accents français
        r'\bChapitre\s+\d+',    # "Chapitre X"
        r"(?:qu'|l'|d'|n'|m'|t'|s'|c')",  # Élisions françaises
    ]
    
    def __init__(self, min_french_score: float = 0.3):
        """
        Args:
            min_french_score: Score minimum pour considérer le texte comme français (0-1)
        """
        self.min_french_score = min_french_score
    
    def validate(self, markdown_path: Path) -> ValidationResult:
        """
        Valide qu'un fichier markdown est en français
        
        Args:
            markdown_path: Chemin vers le fichier .md
            
        Returns:
            ValidationResult avec le résultat de la validation
        """
        if not markdown_path.exists():
            return ValidationResult(
                passed=False,
                message=f"Fichier non trouvé: {markdown_path}",
                details={"path": str(markdown_path)}
            )
        
        if markdown_path.suffix.lower() != '.md':
            return ValidationResult(
                passed=False,
                message=f"Le fichier n'est pas un markdown: {markdown_path.suffix}",
                details={"path": str(markdown_path), "extension": markdown_path.suffix}
            )
        
        # Lire le contenu
        try:
            content = markdown_path.read_text(encoding='utf-8')
        except Exception as e:
            return ValidationResult(
                passed=False,
                message=f"Erreur lors de la lecture du fichier: {str(e)}",
                details={"path": str(markdown_path), "error": str(e)}
            )
        
        # Calculer le score français
        score = self._calculate_french_score(content)
        
        passed = score >= self.min_french_score
        
        return ValidationResult(
            passed=passed,
            message=f"Score français: {score:.2%} ({'suffisant' if passed else 'insuffisant'})",
            details={
                "path": str(markdown_path),
                "french_score": score,
                "min_required": self.min_french_score,
                "file_size": len(content),
                "is_french": passed
            }
        )
    
    def _calculate_french_score(self, text: str) -> float:
        """Calcule un score de "francité" du texte (0-1)"""
        if not text:
            return 0.0
        
        text_lower = text.lower()
        total_indicators = 0
        found_indicators = 0
        
        # 1. Vérifier les mots-clés français
        words = re.findall(r'\b\w+\b', text_lower)
        if words:
            french_word_count = sum(1 for word in words if word in self.FRENCH_KEYWORDS)
            total_indicators += len(words)
            found_indicators += french_word_count * 10  # Pondération forte
        
        # 2. Vérifier les patterns français
        for pattern in self.FRENCH_PATTERNS:
            matches = re.findall(pattern, text_lower)
            found_indicators += len(matches)
            total_indicators += 10  # Base de comparaison
        
        # 3. Vérifier la présence de "Chapitre"
        chapitre_count = len(re.findall(r'\bchapitre\b', text_lower))
        if chapitre_count > 0:
            found_indicators += chapitre_count * 20  # Pondération très forte
            total_indicators += chapitre_count * 20
        
        if total_indicators == 0:
            return 0.0
        
        score = min(found_indicators / total_indicators, 1.0)
        return score


class ChapterStructureValidator:
    """
    Hook 2: Vérifie que le livre est décomposé en chapitres
    et que les titres de chapitres correspondent à ceux du fichier .md
    """
    
    # Patterns de détection de chapitres
    CHAPTER_PATTERNS = [
        r'^#{1,2}\s+(?:\<span[^\>]*\>\</span\>)?\*?\*?Chapitre\s+(\d+)[\.\:]?\s*(.*)$',  # Apprendre LangChain
        r'^#\s+\*?\*?Chapitre\s+(\d+)',  # Le Guide Complet LangGraph
        r'^##\s+\*?\*?Chapitre\s+(\d+)',  # Alternative avec ##
    ]
    
    def __init__(self, min_chapters: int = 1):
        """
        Args:
            min_chapters: Nombre minimum de chapitres requis
        """
        self.min_chapters = min_chapters
    
    def validate(self, markdown_path: Path, json_path: Optional[Path] = None) -> ValidationResult:
        """
        Valide la structure en chapitres d'un livre
        
        Args:
            markdown_path: Chemin vers le fichier .md source
            json_path: Chemin vers le fichier JSON traité (optionnel)
            
        Returns:
            ValidationResult avec le résultat de la validation
        """
        if not markdown_path.exists():
            return ValidationResult(
                passed=False,
                message=f"Fichier markdown non trouvé: {markdown_path}",
                details={"markdown_path": str(markdown_path)}
            )
        
        # Lire le markdown
        try:
            md_content = markdown_path.read_text(encoding='utf-8')
        except Exception as e:
            return ValidationResult(
                passed=False,
                message=f"Erreur lecture markdown: {str(e)}",
                details={"error": str(e)}
            )
        
        # Trouver les chapitres dans le markdown
        md_chapters = self._extract_chapters_from_markdown(md_content)
        
        if len(md_chapters) < self.min_chapters:
            return ValidationResult(
                passed=False,
                message=f"Pas assez de chapitres détectés: {len(md_chapters)} (min: {self.min_chapters})",
                details={
                    "chapters_found": len(md_chapters),
                    "min_required": self.min_chapters,
                    "chapter_titles": [ch['title'] for ch in md_chapters]
                }
            )
        
        # Si un fichier JSON est fourni, vérifier la correspondance
        if json_path and json_path.exists():
            return self._validate_with_json(md_chapters, json_path)
        
        # Sinon, valider uniquement la structure markdown
        return ValidationResult(
            passed=True,
            message=f"{len(md_chapters)} chapitres détectés dans le markdown",
            details={
                "chapters_count": len(md_chapters),
                "chapter_numbers": [ch['number'] for ch in md_chapters],
                "chapter_titles": [ch['title'] for ch in md_chapters]
            }
        )
    
    def _extract_chapters_from_markdown(self, content: str) -> List[Dict]:
        """Extrait les chapitres du markdown"""
        chapters = []
        lines = content.split('\n')
        
        in_code_block = False
        
        for line in lines:
            # Gérer les blocs de code
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                continue
            
            if in_code_block:
                continue
            
            # Tester chaque pattern
            for pattern in self.CHAPTER_PATTERNS:
                match = re.match(pattern, line, re.IGNORECASE | re.MULTILINE)
                if match:
                    chapter_num = int(match.group(1))
                    chapter_title = match.group(2).strip() if len(match.groups()) > 1 else f"Chapitre {chapter_num}"
                    
                    # Nettoyer le titre
                    chapter_title = re.sub(r'<[^>]+>', '', chapter_title).strip()
                    chapter_title = re.sub(r'\*+', '', chapter_title).strip()
                    
                    chapters.append({
                        'number': chapter_num,
                        'title': chapter_title or f"Chapitre {chapter_num}",
                        'line': line.strip()
                    })
                    break
        
        return chapters
    
    def _validate_with_json(self, md_chapters: List[Dict], json_path: Path) -> ValidationResult:
        """Valide la correspondance avec le fichier JSON"""
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            json_chapters = data.get('chapters', [])
            
            if len(md_chapters) != len(json_chapters):
                return ValidationResult(
                    passed=False,
                    message=f"Nombre de chapitres différent: MD={len(md_chapters)}, JSON={len(json_chapters)}",
                    details={
                        "md_chapters": len(md_chapters),
                        "json_chapters": len(json_chapters),
                        "md_titles": [ch['title'] for ch in md_chapters],
                        "json_titles": [ch.get('title', 'N/A') for ch in json_chapters]
                    }
                )
            
            # Vérifier la correspondance des titres
            mismatches = []
            for md_ch, json_ch in zip(md_chapters, json_chapters):
                md_title = md_ch['title'].lower().strip()
                json_title = json_ch.get('title', '').lower().strip()
                
                # Comparaison souple (peut contenir mais pas égalité stricte)
                if md_title and json_title and md_title not in json_title and json_title not in md_title:
                    mismatches.append({
                        'chapter_number': md_ch['number'],
                        'md_title': md_ch['title'],
                        'json_title': json_ch.get('title', 'N/A')
                    })
            
            if mismatches:
                return ValidationResult(
                    passed=False,
                    message=f"{len(mismatches)} titres de chapitres ne correspondent pas",
                    details={
                        "mismatches": mismatches,
                        "total_chapters": len(md_chapters)
                    }
                )
            
            return ValidationResult(
                passed=True,
                message=f"Structure validée: {len(md_chapters)} chapitres correspondent",
                details={
                    "chapters_count": len(md_chapters),
                    "md_chapters": [ch['title'] for ch in md_chapters],
                    "json_chapters": [ch.get('title', 'N/A') for ch in json_chapters]
                }
            )
            
        except Exception as e:
            return ValidationResult(
                passed=False,
                message=f"Erreur validation JSON: {str(e)}",
                details={"error": str(e), "json_path": str(json_path)}
            )


class AudioFileValidator:
    """
    Hook 3: Vérifie que chaque chapitre a son fichier audio associé
    """
    
    def __init__(self, audio_dir: Path = None):
        """
        Args:
            audio_dir: Répertoire racine des fichiers audio
        """
        self.audio_dir = Path(audio_dir or settings.AUDIO_DIR)
    
    def validate(self, book_name: str, json_path: Path) -> ValidationResult:
        """
        Valide que tous les chapitres ont leurs fichiers audio
        
        Args:
            book_name: Nom du livre (dossier dans audio/)
            json_path: Chemin vers le fichier JSON du livre
            
        Returns:
            ValidationResult
        """
        if not json_path.exists():
            return ValidationResult(
                passed=False,
                message=f"Fichier JSON non trouvé: {json_path}",
                details={"json_path": str(json_path)}
            )
        
        # Lire le JSON pour obtenir les chapitres
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            chapters = data.get('chapters', [])
        except Exception as e:
            return ValidationResult(
                passed=False,
                message=f"Erreur lecture JSON: {str(e)}",
                details={"error": str(e)}
            )
        
        if not chapters:
            return ValidationResult(
                passed=False,
                message="Aucun chapitre trouvé dans le JSON",
                details={"json_path": str(json_path)}
            )
        
        # Vérifier les fichiers audio
        book_audio_dir = self.audio_dir / book_name
        
        if not book_audio_dir.exists():
            return ValidationResult(
                passed=False,
                message=f"Répertoire audio non trouvé: {book_audio_dir}",
                details={
                    "book_name": book_name,
                    "audio_dir": str(book_audio_dir),
                    "expected_chapters": len(chapters)
                }
            )
        
        # Chercher les fichiers audio pour chaque chapitre
        missing_audio = []
        found_audio = []
        
        for chapter in chapters:
            chapter_num = chapter.get('number', 0)
            
            # Pattern: BookName_chXX_FULL_*.mp3
            pattern = f"*_ch{chapter_num:02d}_FULL_*.mp3"
            audio_files = list(book_audio_dir.glob(pattern))
            
            if not audio_files:
                missing_audio.append({
                    'chapter_number': chapter_num,
                    'chapter_title': chapter.get('title', 'N/A'),
                    'expected_pattern': pattern
                })
            else:
                found_audio.append({
                    'chapter_number': chapter_num,
                    'chapter_title': chapter.get('title', 'N/A'),
                    'audio_file': str(audio_files[0].name)
                })
        
        if missing_audio:
            return ValidationResult(
                passed=False,
                message=f"{len(missing_audio)}/{len(chapters)} chapitres sans audio",
                details={
                    "missing_audio": missing_audio,
                    "found_audio": found_audio,
                    "total_chapters": len(chapters)
                }
            )
        
        return ValidationResult(
            passed=True,
            message=f"Tous les {len(chapters)} chapitres ont leur audio",
            details={
                "total_chapters": len(chapters),
                "audio_files": found_audio
            }
        )


class AudioAvailabilityValidator:
    """
    Hook 4: Vérifie que tous les audios sont disponibles et correctement associés
    Validation plus approfondie que AudioFileValidator (vérification intégrité, taille, etc.)
    """
    
    MIN_AUDIO_SIZE = 1024  # 1 KB minimum
    
    def __init__(self, audio_dir: Path = None):
        """
        Args:
            audio_dir: Répertoire racine des fichiers audio
        """
        self.audio_dir = Path(audio_dir or settings.AUDIO_DIR)
    
    def validate(self, book_name: str, json_path: Path) -> ValidationResult:
        """
        Valide la disponibilité et l'intégrité de tous les audios
        
        Args:
            book_name: Nom du livre
            json_path: Chemin vers le fichier JSON du livre
            
        Returns:
            ValidationResult
        """
        if not json_path.exists():
            return ValidationResult(
                passed=False,
                message=f"Fichier JSON non trouvé: {json_path}",
                details={"json_path": str(json_path)}
            )
        
        # Lire le JSON
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            chapters = data.get('chapters', [])
        except Exception as e:
            return ValidationResult(
                passed=False,
                message=f"Erreur lecture JSON: {str(e)}",
                details={"error": str(e)}
            )
        
        book_audio_dir = self.audio_dir / book_name
        
        if not book_audio_dir.exists():
            return ValidationResult(
                passed=False,
                message=f"Répertoire audio non trouvé: {book_audio_dir}",
                details={"audio_dir": str(book_audio_dir)}
            )
        
        # Vérifier chaque fichier audio
        validation_errors = []
        valid_audios = []
        
        for chapter in chapters:
            chapter_num = chapter.get('number', 0)
            chapter_title = chapter.get('title', 'N/A')
            
            # Trouver le fichier audio
            pattern = f"*_ch{chapter_num:02d}_FULL_*.mp3"
            audio_files = list(book_audio_dir.glob(pattern))
            
            if not audio_files:
                validation_errors.append({
                    'chapter_number': chapter_num,
                    'chapter_title': chapter_title,
                    'error': 'Fichier audio non trouvé',
                    'expected_pattern': pattern
                })
                continue
            
            audio_file = audio_files[0]
            
            # Vérifier la taille du fichier
            try:
                file_size = audio_file.stat().st_size
                
                if file_size < self.MIN_AUDIO_SIZE:
                    validation_errors.append({
                        'chapter_number': chapter_num,
                        'chapter_title': chapter_title,
                        'error': f'Fichier trop petit ({file_size} bytes)',
                        'audio_file': str(audio_file.name)
                    })
                    continue
                
                # Vérifier que le fichier est lisible
                if not audio_file.is_file():
                    validation_errors.append({
                        'chapter_number': chapter_num,
                        'chapter_title': chapter_title,
                        'error': 'Pas un fichier valide',
                        'audio_file': str(audio_file.name)
                    })
                    continue
                
                valid_audios.append({
                    'chapter_number': chapter_num,
                    'chapter_title': chapter_title,
                    'audio_file': str(audio_file.name),
                    'file_size': file_size,
                    'file_size_mb': round(file_size / (1024 * 1024), 2)
                })
                
            except Exception as e:
                validation_errors.append({
                    'chapter_number': chapter_num,
                    'chapter_title': chapter_title,
                    'error': f'Erreur accès fichier: {str(e)}',
                    'audio_file': str(audio_file.name) if audio_file else 'N/A'
                })
        
        if validation_errors:
            return ValidationResult(
                passed=False,
                message=f"{len(validation_errors)}/{len(chapters)} audios invalides ou manquants",
                details={
                    "validation_errors": validation_errors,
                    "valid_audios": valid_audios,
                    "total_chapters": len(chapters)
                }
            )
        
        total_size = sum(a['file_size'] for a in valid_audios)
        
        return ValidationResult(
            passed=True,
            message=f"Tous les {len(chapters)} audios sont disponibles et valides",
            details={
                "total_chapters": len(chapters),
                "total_size_mb": round(total_size / (1024 * 1024), 2),
                "audio_files": valid_audios
            }
        )


def validate_book_pipeline(
    book_name: str,
    markdown_path: Path,
    json_path: Optional[Path] = None,
    skip_checks: Optional[List[str]] = None
) -> Dict[str, ValidationResult]:
    """
    Exécute tous les hooks de validation pour un livre
    
    Args:
        book_name: Nom du livre (pour les fichiers audio)
        markdown_path: Chemin vers le fichier .md source
        json_path: Chemin vers le fichier JSON traité (optionnel)
        skip_checks: Liste des checks à ignorer ['french', 'structure', 'audio', 'availability']
        
    Returns:
        Dict avec les résultats de chaque validation
    """
    skip_checks = skip_checks or []
    results = {}
    
    # Hook 1: Vérifier que c'est du français
    if 'french' not in skip_checks:
        french_validator = FrenchMarkdownValidator()
        results['french'] = french_validator.validate(markdown_path)
    
    # Hook 2: Vérifier la structure en chapitres
    if 'structure' not in skip_checks:
        structure_validator = ChapterStructureValidator()
        results['structure'] = structure_validator.validate(markdown_path, json_path)
    
    # Hook 3 & 4: Vérifier les audios (seulement si JSON fourni)
    if json_path and json_path.exists():
        if 'audio' not in skip_checks:
            audio_validator = AudioFileValidator()
            results['audio'] = audio_validator.validate(book_name, json_path)
        
        if 'availability' not in skip_checks:
            availability_validator = AudioAvailabilityValidator()
            results['availability'] = availability_validator.validate(book_name, json_path)
    
    return results
