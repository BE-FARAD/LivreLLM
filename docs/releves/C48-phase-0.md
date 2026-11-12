# C48 — phase 0 : cadrage, nettoyage, environnement figé

**Session r01 du PC bureau, 2026-11-12.** Dépôt `BE-FARAD/LivreLLM`, worktree
`livrellm-wt\c48`, branche `feat/c48-amelioration`. Consigne
`consignes-r01-C48-LivreLLM-amelioration.md`, plan de référence
`plan-amelioration-LivreLLM-BOSQUEL.md` et son amendement 1.

Test d'acceptation de la phase, tel que C48 l'énonce : **« l'application
démarre depuis une installation neuve, suite de tests verte »**. Il est passé,
et la mesure est plus bas.

## Ce que la phase 0 devait trancher

C48 ne laisse pas le cadrage ouvert : ses décisions 1 et 4 le tranchent déjà.
La phase 0 ne décide donc rien — elle **applique**, et elle oppose ce qu'elle
applique à un test, pour qu'une session suivante ne puisse pas le défaire sans
le savoir.

## 1. Le paquet porte enfin un nom

Le code vivait sous `src/`, et s'importait `from src.conversion…`. Un paquet
qui s'appelle du nom de son dossier ne s'importe que depuis la racine du
dépôt : LivreLLM ne **pouvait pas** devenir « une bibliothèque Python
importable », ce que la décision 1 de C48 lui demande d'être. Le code a
déménagé dans `src/livrellm/`, les vingt fichiers qui l'importaient ont suivi,
et `pyproject.toml` déclare un vrai paquet (`hatchling`, `packages =
["src/livrellm"]`), comme `outil-reprise-conception` déclare `reprise`.

`config/`, lui, **n'est pas** installé : c'est la configuration d'un poste, un
poste la remplit, il ne l'importe pas depuis une roue. Un `conftest.py` à la
racine pose le dépôt en tête de `sys.path`, une fois, plutôt que dans chaque
test.

## 2. Un seul cadre d'application — et les deux partent

Le dépôt portait **deux** interfaces à la fois : Streamlit (`app/`) et Flask
(`web_app/`). Deux interfaces à tenir d'accord pour une seule bibliothèque, et
aucune des deux n'est celle que l'outil emploie. Le plan du 10/11 laissait le
choix entre elles ouvert pour AF ; C48 décision 1 le tranche en retirant **les
deux** : LivreLLM devient une bibliothèque plus une vue de `src/reprise/ihm`.

Les deux dossiers, et la sauvegarde `_backup_old_app/`, sont **rangés et non
supprimés** sous `_range/2026-11-12_c48/`, avec un LISEZ-MOI qui dit ce qui
vient d'où, pourquoi, et ce qu'il faudrait pour les relancer. Ils ne sont ni
lintés (`extend-exclude` de `ruff`) ni testés : **on les relit tels qu'ils
étaient**, on ne les répare pas à leur insu — leurs `from src.…` d'origine sont
gardés exprès.

## 3. Les dépendances déclarées sont celles que le code emploie

Mesuré, pas supposé : un parcours de l'arbre syntaxique de tout le chemin
principal (`src/`, `config/`, `scripts/`, `tests/`). **Quatre dépendances
étaient déclarées et importées par rien** — ni par le chemin principal, ni même
par les interfaces rangées : `pydub`, `httpx`, `langdetect`, `markdown`. Elles
pesaient sur chaque installation neuve sans que personne ne sache pourquoi.
Elles sortent, avec `streamlit` et `flask` qui partent avec leur cadre.

Deux restent déclarées **sans être importées**, et chacune pour une raison
écrite :

| Déclarée | Pourquoi, alors que rien ne l'importe |
|---|---|
| `marker-pdf==1.10.2` | `marker_converter.py` l'appelle **en ligne de commande** (`marker_single`). Le test ne l'exempte pas à l'aveugle : il vérifie que cette commande est bien nommée dans les sources. |
| `torch>=2.9` | Déclarée **uniquement pour que l'index CUDA ait prise sur elle** (voir § 4). Opposée par son propre test, pas par une tolérance. |

`tests/test_phase0_cadrage.py` oppose la liste au code **dans les deux sens** :
un import non déclaré échoue, et une dépendance que personne n'emploie échoue
aussi. C'est le second sens qui avait mordu.

## 4. `torch` venait de PyPI, c'est-à-dire sans CUDA

**Le défaut qui comptait le plus de cette phase, et il ne se voyait pas.** C48
demande `torch` depuis l'index CUDA 12.8. Déclarer `[tool.uv.sources]` ne
suffisait pas : une *source* `uv` ne s'applique qu'à une dépendance **directe**,
et tant que `torch` n'arrivait que par `marker-pdf`, il était résolu depuis
PyPI — c'est-à-dire, sur Windows, **la roue sans CUDA**. Les scans se seraient
convertis sur le processeur, et **rien ne l'aurait dit** : pas d'erreur, pas
d'avertissement, juste une conversion lente qu'on aurait mise sur le compte du
volume.

Mesure, avant et après, sur la même machine :

| | Avant | Après |
|---|---|---|
| `torch` au verrou | `2.9.1`, `registry = "https://pypi.org/simple"` | `2.11.0+cu128`, `registry = "https://download.pytorch.org/whl/cu128"` |
| `torch.cuda.is_available()` | — | `True` |
| Appareil vu | — | `NVIDIA GeForce RTX 5070` |

`test_torch_vient_de_l_index_cuda` lit **`uv.lock`**, pas seulement
`pyproject.toml` : c'est le verrou qui dit d'où la roue vient, et c'est donc lui
qu'il faut opposer. La **mesure du gain réel** sur une conversion — ce que C48
appelle « contrôler que le GPU est réellement utilisé » — est le travail de la
phase 1 : elle a besoin d'un document à convertir, et la phase 0 n'en ingère
aucun.

## 5. Le chat partait vers un service externe, par défaut et en silence

`config/settings.py` portait `LLM_PROVIDER`, `OLLAMA_HOST` et `OLLAMA_MODEL`.
`LLMClient` ne les lisait **pas** : il construisait un `OpenAI(...)` et s'en
tenait là. Le réglage existait, le choix n'existait pas. La décision 4 de C48
dit l'inverse — *modèle local par défaut ; aucun contenu de norme, de TI ou de
pièce client n'est envoyé à un service externe* — et c'est à la phase 2, quand
des morceaux de norme entreront dans le corps des messages, que ce défaut aurait
coûté cher.

Le défaut est désormais `ollama`, le client lit le réglage, et un fournisseur
distant ne se joint que si le réglage le **nomme**.

**Deuxième défaut du même fichier, de la même famille que C44** : `chat()`
attrapait toute exception et rendait la chaîne `f"Error: {e}"`. Pour l'appelant,
c'était une réponse du modèle comme une autre — affichable, indexable,
citable. Une panne lève maintenant `ErreurDeChat`. Deux cas l'opposent : un hôte
Ollama muet, et `openai` sans clé, qui refuse **avant** de tenter l'appel.

**Limite à connaître, écrite plutôt que masquée** : il n'existe pas encore de
chemin local pour la **synthèse vocale**. `tts_service.py` appelle OpenAI, et
rien d'autre. `TTS_PROVIDER` reste donc à `openai`, et `.env.example` le dit en
toutes lettres : un texte lu à voix haute part vers un service externe. Écrire
un défaut local qui ne marcherait pas aurait été un mensonge de plus.

## 6. Ce que `ruff` a trouvé en passant

Soixante-quatre signalements sur le code hérité, dont **cinquante-cinq**
réparés par `ruff --fix`. Les neuf autres ont été lus un par un, et trois
étaient des défauts réels, pas des questions de style :

- `scripts/import_learning_langchain.py` — **ce script n'a jamais pu tourner**.
  Deux `NameError` : une boucle `for pattern in patterns` alors que seul
  `pattern` est construit, et un appel à `parse_chapters_smart(content,
  book_name)`, fonction qui n'existe nulle part — la seule que le fichier
  définisse est `parse_chapters_langchain(text)`. Réparé au plus près de
  l'intention lisible : `patterns = [pattern]`, et l'appel à la fonction qui
  existe. On n'a pas inventé les motifs qui manquaient peut-être.
- `src/livrellm/storage/image_manager.py` — `Optional` employé en annotation
  sans être importé : `NameError` à l'import du module.
- `src/livrellm/conversion/marker_converter.py` — deux lignes **inatteignables**
  après un `raise` : le message d'erreur détaillé de `marker` n'a jamais été
  affiché. Le détail est gardé, et la levée se fait une seule fois.

## 7. Environnement épinglé

Même dispositif que C11 dans le dépôt outil, et pour la même raison mesurée :
`uv.lock` fixe les dépendances, **pas** l'interprète ni l'outil qui résout.

- `.python-version` : `3.12.16`, le correctif **exact** ;
- `[tool.uv] python-preference = "only-managed"` — ce poste porte plus d'un
  interprète 3.12, et le PATH n'est pas une garantie ;
- `[tool.uv] required-version = ">=0.13.6,<0.14"`.

Le test ne lit pas que le fichier : il compare `.python-version` à
**l'interprète qui tourne**. Un fichier d'épinglage que personne n'applique
n'épingle rien.

## Vérifié, pas supposé

| Quoi | Résultat |
|---|---|
| `uv run ruff check .` | `All checks passed!` |
| `uv run pytest -q` | **26 passed** (dont les **16 cas neufs** de `test_phase0_cadrage.py`) |
| Installation **neuve** depuis le verrou, dans un environnement séparé (`UV_PROJECT_ENVIRONMENT`, `uv sync --frozen`) | voir la ligne d'état de la session |
| `torch.cuda.is_available()` | `True`, RTX 5070 |
| Fichier supprimé dans le diff | **aucun** — trois dossiers **renommés** vers `_range/` |

## Ce qui n'est pas fait, et ne prétend pas l'être

- **Aucun document n'est ingéré** : la liste des documents des bibliothèques
  BOSQUEL, l'édition, l'empreinte et le repère de page sont le travail de la
  phase 1, et C48 demande que cette liste soit écrite **avant** l'ingestion.
- **Le gain GPU n'est pas mesuré** sur une conversion réelle (phase 1).
- **Aucune vue n'est écrite dans `src/reprise/ihm`** : la décision 1 dit où
  LivreLLM s'affichera, la phase 0 le rend seulement *importable*.
- `EMBEDDING_MODEL` est un réglage **que rien ne lit** : `embedding_service.py`
  fixe lui-même un modèle local. Gardé tel quel et signalé, plutôt que corrigé
  en douce : la phase 1 dira où ce choix vit.

## Un point pour AF, non bloquant

**Le dépôt `BE-FARAD/LivreLLM` est public.** Les phases 1 et 2 doivent y faire
entrer les pièces d'affaires — CCTP, spécifications, pièces Patriarche — et des
bibliothèques nommées par affaire. La règle de la liste noire (aucun nom de
client, d'affaire ou de site dans un dépôt) et T9 s'y appliquent comme ailleurs,
mais un dépôt public ne laisse aucune seconde chance : ce qui y est poussé une
fois est indexable même retiré. Porté dans `pour-AF.md`. Rien n'a été ingéré à
ce stade, donc rien n'est exposé.
