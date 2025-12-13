# Valider une classe

Vérifie que la classe `$ARGUMENTS` est prête pour validation :

## Checklist automatique

1. **Conformité UML**
   - [ ] Tous les attributs présents
   - [ ] Toutes les méthodes présentes
   - [ ] Types conformes

2. **Tests**
   - [ ] Fichier test existe : `tests/test_$ARGUMENTS.py`
   - [ ] Tous les tests passent
   - [ ] Couverture > 80%

3. **Qualité**
   - [ ] `ruff check src/` sans erreur
   - [ ] Docstrings présentes

4. **Mise à jour CLAUDE.md**
   - Cocher la classe dans la checklist

## Demande de validation

Afficher le résumé et demander :
> "La classe $ARGUMENTS est-elle validée ? (oui/non)"

Si oui → Mettre à jour CLAUDE.md
Si non → Lister les corrections nécessaires
