# Exécuter les tests

Exécute les tests pour `$ARGUMENTS` :

```bash
pytest tests/test_$ARGUMENTS.py -v --cov=src/ --cov-report=term-missing
```

Si aucun argument :
```bash
pytest tests/ -v --cov=src/ --cov-report=term-missing
```

Affiche :
1. Résultat des tests (pass/fail)
2. Couverture de code
3. Lignes non couvertes

⚠️ Tous les tests doivent passer avant validation.
