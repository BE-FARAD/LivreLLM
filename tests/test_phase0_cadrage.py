"""Phase 0 de C48 — ce que le cadrage promet, oppose au depot.

Un nettoyage qu'aucun test ne lit se defait en silence : il suffit qu'une
session remette un `import streamlit` sur le chemin principal, ou qu'une
dependance revienne dans `pyproject.toml` sans que rien ne l'importe, et le
cadrage n'existe plus sans que personne ne l'ait decide. Ce fichier lit donc
**les sources et le fichier de projet**, et oppose les cinq promesses de la
phase 0 l'une apres l'autre.

Chaque verification se fait **dans les deux sens** quand les deux sens ont un
sens : un import non declare echoue, et une dependance que nul n'importe echoue
aussi.
"""

from __future__ import annotations

import ast
import pathlib
import sys
import tomllib

import pytest

RACINE = pathlib.Path(__file__).resolve().parent.parent
RANGE = RACINE / "_range" / "2026-11-12_c48"

#: Les dossiers du **chemin principal** : ceux que `ruff` lint, que `pytest`
#: lance, et que le paquet importe. `_range/` n'en est pas, par construction.
CHEMIN_PRINCIPAL = ("src", "config", "scripts", "tests")

#: Nom de distribution -> nom du module que l'on ecrit dans un `import`.
#: Les deux different assez souvent pour qu'une comparaison naive se trompe.
MODULE_DE_LA_DISTRIBUTION = {
    "python-dotenv": "dotenv",
    "qdrant-client": "qdrant_client",
    "marker-pdf": "marker",
}

#: `marker-pdf` est declare sans etre importe, et c'est **voulu** :
#: `marker_converter.py` l'appelle en ligne de commande (`marker_single`). Le
#: test ci-dessous ne se contente pas de l'exempter — il verifie que cette
#: commande est bien nommee quelque part dans les sources.
DECLAREES_SANS_IMPORT = {"marker-pdf": "marker_single"}

#: `torch` est declare sans etre ni importe ni appele : il est ecrit uniquement
#: pour que `[tool.uv.sources]` ait prise sur lui — une source ne s'applique
#: qu'a une dependance **directe**. Son exemption est donc d'une autre nature
#: que celle de `marker-pdf`, et elle est opposee par son propre test
#: (`test_torch_vient_de_l_index_cuda`), pas par une simple tolerance.
DECLAREE_POUR_SON_INDEX = {"torch"}


def _pyproject() -> dict:
    return tomllib.loads((RACINE / "pyproject.toml").read_text(encoding="utf-8"))


def _fichiers_du_chemin_principal() -> list[pathlib.Path]:
    fichiers: list[pathlib.Path] = []
    for dossier in CHEMIN_PRINCIPAL:
        for p in sorted((RACINE / dossier).rglob("*.py")):
            if "__pycache__" in p.parts:
                continue
            fichiers.append(p)
    return fichiers


def _modules_importes(fichier: pathlib.Path) -> set[str]:
    arbre = ast.parse(fichier.read_text(encoding="utf-8"))
    noms: set[str] = set()
    for noeud in ast.walk(arbre):
        if isinstance(noeud, ast.Import):
            noms.update(alias.name.split(".")[0] for alias in noeud.names)
        elif isinstance(noeud, ast.ImportFrom) and noeud.level == 0 and noeud.module:
            noms.add(noeud.module.split(".")[0])
    return noms


# --- 1. Le paquet porte un nom, et plus rien ne s'importe par `src` ----------


def test_le_paquet_s_appelle_livrellm_et_s_importe() -> None:
    """Il s'appelait `src`, donc il ne s'importait que depuis la racine."""
    import livrellm  # noqa: F401  (l'import **est** la verification)

    assert (RACINE / "src" / "livrellm" / "__init__.py").exists()
    assert _pyproject()["project"]["name"] == "livrellm"


def test_aucun_import_par_le_nom_du_dossier_src() -> None:
    fautifs = [
        p.relative_to(RACINE).as_posix()
        for p in _fichiers_du_chemin_principal()
        if "src" in _modules_importes(p)
    ]
    assert fautifs == [], f"ces fichiers importent encore le dossier `src` : {fautifs}"


# --- 2. Un seul cadre : les deux interfaces sont rangees, pas supprimees -----


def test_les_deux_interfaces_sont_rangees_et_toujours_la() -> None:
    """Rangees, **jamais supprimees** : le dossier et son LISEZ-MOI existent."""
    assert (RANGE / "LISEZ-MOI.md").exists()
    assert (RANGE / "app-streamlit").is_dir()
    assert (RANGE / "web_app-flask").is_dir()
    assert not (RACINE / "app").exists()
    assert not (RACINE / "web_app").exists()


@pytest.mark.parametrize("cadre", ["streamlit", "flask"])
def test_aucun_cadre_d_application_sur_le_chemin_principal(cadre: str) -> None:
    fautifs = [
        p.relative_to(RACINE).as_posix()
        for p in _fichiers_du_chemin_principal()
        if cadre in _modules_importes(p)
    ]
    assert fautifs == [], f"`{cadre}` est revenu sur le chemin principal : {fautifs}"


@pytest.mark.parametrize("cadre", ["streamlit", "flask", "markdown"])
def test_aucun_cadre_d_application_n_est_plus_declare(cadre: str) -> None:
    declarees = _pyproject()["project"]["dependencies"]
    assert not any(d.split(">")[0].split("=")[0].strip() == cadre for d in declarees)


# --- 3. Les dependances declarees sont celles que le code emploie ------------


def _declarees() -> set[str]:
    return {
        d.replace("==", ">").replace(">=", ">").split(">")[0].strip()
        for d in _pyproject()["project"]["dependencies"]
    }


def _importees() -> set[str]:
    noms: set[str] = set()
    for p in _fichiers_du_chemin_principal():
        noms |= _modules_importes(p)
    return noms


def test_tout_module_tiers_importe_est_declare() -> None:
    """Sens 1 : rien ne s'importe qui ne soit ecrit dans `pyproject.toml`."""
    connus = {MODULE_DE_LA_DISTRIBUTION.get(d, d.replace("-", "_")) for d in _declarees()}
    locaux = {"livrellm", "config", "pytest", "tests", "scripts"}
    inconnus = {
        m
        for m in _importees()
        if m not in connus and m not in locaux and m not in sys.stdlib_module_names
    }
    assert inconnus == set(), f"importes mais non declares : {sorted(inconnus)}"


def test_toute_dependance_declaree_est_employee() -> None:
    """Sens 2 : rien n'est declare que personne n'emploie.

    C'est ce sens-la qui a mordu : quatre dependances — `pydub`, `httpx`,
    `langdetect`, `markdown` — etaient declarees et importees **par rien**, ni
    par le chemin principal ni par le cadre range. Elles pesaient sur chaque
    installation neuve sans que personne ne sache pourquoi.
    """
    importees = _importees()
    orphelines = []
    for distribution in sorted(_declarees() - DECLAREE_POUR_SON_INDEX):
        module = MODULE_DE_LA_DISTRIBUTION.get(distribution, distribution.replace("-", "_"))
        if module in importees:
            continue
        commande = DECLAREES_SANS_IMPORT.get(distribution)
        if commande and any(
            commande in p.read_text(encoding="utf-8") for p in _fichiers_du_chemin_principal()
        ):
            continue  # appelee en ligne de commande, et la commande est bien la
        orphelines.append(distribution)
    assert orphelines == [], f"declarees mais employees par rien : {orphelines}"


# --- 4. L'environnement est epingle ------------------------------------------


def test_le_correctif_de_python_est_epingle_et_c_est_celui_qui_tourne() -> None:
    """Le fichier ne vaut que si l'interprete du jour lui obeit."""
    epingle = (RACINE / ".python-version").read_text(encoding="utf-8").strip()
    assert epingle.count(".") == 2, f".python-version doit porter le correctif exact : {epingle}"
    qui_tourne = ".".join(str(n) for n in sys.version_info[:3])
    assert qui_tourne == epingle, f"epingle {epingle}, mais c'est {qui_tourne} qui tourne"


def test_uv_ne_prend_que_les_interpretes_qu_il_gere() -> None:
    outil_uv = _pyproject()["tool"]["uv"]
    assert outil_uv["python-preference"] == "only-managed"
    assert outil_uv["required-version"].startswith(">=")


def test_le_convertisseur_est_fige_a_l_egal() -> None:
    """Une version de `marker` qui bouge deplace la pagination de sa sortie."""
    declarees = _pyproject()["project"]["dependencies"]
    marker = [d for d in declarees if d.startswith("marker-pdf")]
    assert marker == ["marker-pdf==1.10.2"], marker


def test_torch_vient_de_l_index_cuda() -> None:
    """Et le verrou doit le montrer, pas seulement le fichier de projet.

    Declarer l'index ne suffit pas : tant que `torch` n'arrivait que par
    `marker`, `[tool.uv.sources]` n'avait aucune prise sur lui — une source ne
    s'applique qu'a une dependance directe — et il etait resolu depuis PyPI,
    c'est-a-dire, sur Windows, **sans CUDA**. On lit donc `uv.lock`.
    """
    projet = _pyproject()
    index = {i["name"]: i["url"] for i in projet["tool"]["uv"]["index"]}
    assert "cu128" in index["pytorch-cu128"]
    assert projet["tool"]["uv"]["sources"]["torch"][0]["index"] == "pytorch-cu128"
    assert any(d.startswith("torch") for d in projet["project"]["dependencies"])

    verrou = tomllib.loads((RACINE / "uv.lock").read_text(encoding="utf-8"))
    torch = next(p for p in verrou["package"] if p["name"] == "torch")
    assert "cu128" in torch["source"].get("registry", ""), torch["source"]


# --- 5. Le chat est local par defaut, et une panne n'est pas une reponse -----


def test_le_fournisseur_de_chat_par_defaut_est_local() -> None:
    from config.settings import Settings
    from livrellm.llm.llm_client import FOURNISSEUR_LOCAL

    assert Settings.LLM_PROVIDER == FOURNISSEUR_LOCAL


def test_le_client_sans_reglage_est_local() -> None:
    from livrellm.llm.llm_client import LLMClient

    client = LLMClient()
    assert client.est_local, f"fournisseur par defaut : {client.fournisseur}"


def test_un_fournisseur_inconnu_est_refuse_et_non_devine() -> None:
    from livrellm.llm.llm_client import FournisseurInconnu, LLMClient

    with pytest.raises(FournisseurInconnu):
        LLMClient(fournisseur="un-service-qui-n-existe-pas")


def test_une_panne_leve_au_lieu_de_rendre_une_reponse() -> None:
    """Le defaut ferme : `chat()` rendait la chaine `"Error: ..."`.

    L'appelant ne pouvait pas la distinguer d'une reponse du modele : il
    pouvait l'afficher, l'indexer, la citer. On pointe le client local vers un
    hote qui ne repond pas, et on exige une exception.
    """
    from livrellm.llm import llm_client as module
    from livrellm.llm.llm_client import ErreurDeChat, LLMClient

    client = LLMClient(fournisseur="ollama", modele="modele-absent")
    hote_d_origine = module.settings.OLLAMA_HOST
    module.settings.OLLAMA_HOST = "http://127.0.0.1:9"  # port « discard », muet
    try:
        with pytest.raises(ErreurDeChat):
            client.chat([{"role": "user", "content": "bonjour"}])
    finally:
        module.settings.OLLAMA_HOST = hote_d_origine


def test_openai_sans_cle_refuse_avant_tout_appel() -> None:
    from livrellm.llm import llm_client as module
    from livrellm.llm.llm_client import ErreurDeChat, LLMClient

    client = LLMClient(fournisseur="openai", modele="un-modele")
    cle_d_origine = module.settings.OPENAI_API_KEY
    module.settings.OPENAI_API_KEY = None
    try:
        with pytest.raises(ErreurDeChat, match="OPENAI_API_KEY"):
            client.chat([{"role": "user", "content": "bonjour"}])
    finally:
        module.settings.OPENAI_API_KEY = cle_d_origine
