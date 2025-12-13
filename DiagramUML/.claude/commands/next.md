# Prochaine étape

Détermine et affiche la prochaine classe à implémenter :

1. **Lire** `CLAUDE.md` pour trouver la première classe non validée
2. **Vérifier** que ses dépendances sont validées
3. **Afficher** les informations de la classe depuis `docs/specifications/specifications.md`
4. **Afficher** les attributs/méthodes depuis le diagramme UML

## Format de sortie

```
═══════════════════════════════════════════
        PROCHAINE CLASSE À IMPLÉMENTER
═══════════════════════════════════════════

Classe    : FileWatcher
Package   : src/input/
Fichier   : src/input/file_watcher.py
Test      : tests/test_file_watcher.py

───────────────────────────────────────────
DÉPENDANCES
───────────────────────────────────────────
✓ QdrantClient (validé)

───────────────────────────────────────────
ATTRIBUTS
───────────────────────────────────────────
- inputDirectory: String = "01-input"
- qdrantClient: QdrantClient

───────────────────────────────────────────
MÉTHODES
───────────────────────────────────────────
+ scanOnStartup(): List<File>
+ scanOnUserClick(): List<File>
+ checkFileExists(file: File): bool
+ computeHash(file: File): String
+ validatePDF(file: File): bool
+ getNewFiles(): List<File>

═══════════════════════════════════════════
Lancer /implement-class FileWatcher pour commencer
═══════════════════════════════════════════
```
