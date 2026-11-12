# Ce qui a été rangé le 2026-11-12 par la phase 0 de C48

**Rien n'a été supprimé.** Trois dossiers ont quitté le chemin principal et
dorment ici, tels qu'ils étaient le jour où ils ont été rangés. Ils ne sont ni
lintés (`extend-exclude` de `ruff`), ni testés, ni importés par le paquet
`livrellm`. AF seul décide de leur sort.

| Rangé ici | Venait de | Pourquoi |
|---|---|---|
| `app-streamlit/` | `app/` | Interface Streamlit |
| `web_app-flask/` | `web_app/` | Interface Flask |
| `_backup_old_app/` | `_backup_old_app/` | Sauvegarde de l'application d'avant, déjà hors du code |

## Pourquoi les deux interfaces partent ensemble

La décision 1 de la consigne C48 d'AF : **LivreLLM devient une bibliothèque
Python importable plus une vue de l'interface de l'outil** (`src/reprise/ihm`
du dépôt `outil-reprise-conception`), **pas une application à part**. Le dépôt
en portait deux à la fois — Streamlit et Flask —, c'est-à-dire deux interfaces à
tenir d'accord pour une seule bibliothèque, et aucune des deux n'était celle que
l'outil emploie. Le plan d'amélioration du 2026-11-10 laissait le choix entre
les deux ouvert pour AF ; C48 le tranche en en retirant **les deux**.

## Ce que cela coûte à qui voudrait les relancer

Leurs deux dépendances, `streamlit` et `flask`, **ne sont plus déclarées** dans
`pyproject.toml`, non plus que `markdown`, qui ne servait qu'au gabarit Flask.
Pour relancer l'une de ces interfaces telle quelle, il faut donc les réinstaller
à la main, et corriger ses imports : le paquet s'appelle désormais `livrellm` et
non `src`. Le code rangé ici porte encore ses `from src.…` d'origine, **et c'est
voulu** — on le relit tel qu'il était, on ne le répare pas à son insu.

## Ce qui n'a pas bougé

`scripts/`, `config/`, `data/`, `tests/` et la documentation restent sur le
chemin principal. Les scripts ont, eux, **reçu** le nouveau nom de paquet : ils
servent encore.
