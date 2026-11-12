"""Racine de la suite de tests.

Deux paquets cohabitent dans ce depot, et ils ne s'installent pas de la meme
facon :

- `livrellm`, sous `src/`, est **le** paquet du projet : `pyproject.toml` le
  declare, et `uv` l'installe en mode editable. Il s'importe par son nom depuis
  n'importe ou ;
- `config`, a la racine, est la configuration d'un poste. Elle n'est pas
  livree avec la bibliotheque — un poste la remplit, il ne l'importe pas depuis
  une roue — et elle n'est donc pas installee.

Sans la ligne ci-dessous, `from config.settings import settings` ne trouve rien
des que `pytest` tourne autrement que depuis la racine. On pose donc la racine
du depot en tete de `sys.path`, une fois, ici, plutot que dans chaque test.
"""

import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parent

if str(RACINE) not in sys.path:
    sys.path.insert(0, str(RACINE))
