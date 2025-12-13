# Analyse du Projet Existant - _LivreLLM

## Vue d'ensemble

Le projet `_LivreLLM` est une application fonctionnelle de lecture de livres techniques avec interaction LLM.

**Statut : Fonctionnel mais mal structuré**

---

## Ce qui a été réalisé correctement

### 1. Conversion PDF → Markdown (Marker)

**Fichier :** `core/scanner.py`

| Aspect | Implémentation | Qualité |
|--------|----------------|---------|
| Appel Marker CLI | `marker_single` via subprocess | ✅ Bon |
| Gestion des versions | Fallback syntaxe ancienne | ✅ Bon |
| Recherche du .md | Candidates + recherche récursive | ✅ Robuste |
| Gestion erreurs | try/except + messages clairs | ✅ Bon |

**Code réutilisable :**
```python
# core/scanner.py - Fonction scan_pdf_with_marker()
# Gère bien les différentes versions de Marker
# Recherche intelligente du fichier .md généré
```

---

### 2. Base Vectorielle (Qdrant + FastEmbed)

**Fichier :** `backend/services/vector_service.py`

| Aspect | Implémentation | Qualité |
|--------|----------------|---------|
| Client Qdrant | Singleton global | ✅ Bon |
| Embeddings | FastEmbed (BAAI/bge-small-en-v1.5) | ✅ Local, gratuit |
| Création collection | Auto si inexistante | ✅ Bon |
| Recherche | Cosine similarity | ✅ Standard |

**Code réutilisable :**
```python
# VectorService avec FastEmbed local (pas d'API payante)
# Modèle : BAAI/bge-small-en-v1.5 (384 dimensions)
# Stockage local : path="qdrant_db"
```

---

### 3. Service LLM (Multi-provider)

**Fichier :** `backend/services/llm_service.py`

| Aspect | Implémentation | Qualité |
|--------|----------------|---------|
| Providers | OpenAI, Grok, Anthropic | ✅ Flexible |
| Traduction | Prompt français | ✅ Fonctionnel |
| Résumé | summarize_chapter() | ✅ Fonctionnel |
| Q&A | answer_question() avec contexte | ✅ RAG basique |
| Contextualisation | contextualize_chunk() | ✅ Avancé |
| Graph extraction | extract_graph_entities() | ⚠️ Prévu mais non utilisé |

**Code réutilisable :**
```python
# LLMService - Support multi-providers
# Méthode contextualize_chunk() pour contextual embeddings
# Réponses en français par défaut
```

---

### 4. Interface Streamlit

**Fichier :** `app.py`

| Aspect | Implémentation | Qualité |
|--------|----------------|---------|
| Navigation | Sidebar + sélection livre | ✅ Fonctionnel |
| Thème | Clair/Sombre (Apple Books style) | ✅ Beau |
| Lecture chapitres | Sélecteur + affichage Markdown | ✅ Fonctionnel |
| Chat LLM | Interface conversationnelle | ✅ Fonctionnel |
| TTS | OpenAI tts-1 + autoplay | ✅ Fonctionnel |
| Surlignage | Couleurs + sauvegarde | ✅ Bonus |
| Langue | Toggle FR/EN | ✅ Fonctionnel |

**Code réutilisable :**
```python
# CSS Apple Books style
# Grille de livres avec cartes colorées
# Chat intégré avec RAG
# Lecteur audio intégré
```

---

### 5. TTS (Text-to-Speech)

**Fichier :** `backend/routers/tts.py`

| Aspect | Implémentation | Qualité |
|--------|----------------|---------|
| API | OpenAI tts-1 | ✅ Simple |
| Voix | "alloy" | ✅ Fonctionnel |
| Format | audio/mpeg | ✅ Standard |

**Code réutilisable :**
```python
# Endpoint FastAPI /tts/
# Retourne directement le contenu audio
```

---

### 6. Traitement des livres

**Dans :** `app.py` - fonction `process_new_files()`

| Aspect | Implémentation | Qualité |
|--------|----------------|---------|
| Scan dossier | 01_INPUTS/ | ✅ Fonctionnel |
| Découpage chapitres | Regex sur # | ⚠️ Basique |
| Traduction auto | GPT-4o par chapitre | ✅ Fonctionnel |
| Indexation RAG | chunk_text() + index_document() | ✅ Fonctionnel |
| Métadonnées | metadata.json | ✅ Fonctionnel |
| Archivage PDF | Déplacé vers processed/ | ✅ Bon |

---

## Problèmes de structure identifiés

### 1. Code monolithique

```
app.py = 760+ lignes avec TOUT dedans :
- UI Streamlit
- Logique métier
- Accès base de données
- Traitement PDF
- TTS
- Chat
```

**Impact :** Difficile à maintenir, tester, réutiliser

---

### 2. Duplication de code

| Code | Présent dans |
|------|--------------|
| QdrantClient | `app.py` ET `vector_service.py` |
| OpenAI client | `app.py` ET `llm_service.py` ET `tts.py` |
| Chunking | `app.py` ET `ingestion_service.py` |

---

### 3. Backend non utilisé

```
backend/
├── main.py              # FastAPI jamais lancé
├── routers/             # Endpoints jamais utilisés
└── services/            # Services jamais appelés depuis app.py
```

L'app Streamlit (`app.py`) fait tout en local au lieu d'appeler le backend FastAPI.

---

### 4. Structure de données incohérente

```
library_data/{book_id}/
├── metadata.json
├── content.md
├── chapter_1.txt        # Original
├── chapter_1_fr.txt     # Traduit (parfois identique)
├── chapter_1_en.txt     # Parfois dupliqué
├── audio_chap_1.mp3
└── highlights_chap_1.json
```

Pas de structure claire FR/EN séparée.

---

## Comment exploiter ce projet

### 1. Récupérer le code fonctionnel

| Composant | Fichier source | À intégrer dans |
|-----------|----------------|-----------------|
| Scanner Marker | `core/scanner.py` | `src/conversion/marker_converter.py` |
| VectorService | `backend/services/vector_service.py` | `src/vectorization/vector_store.py` |
| LLMService | `backend/services/llm_service.py` | `src/llm/llm_client.py` |
| TTS | `backend/routers/tts.py` | `src/storage/tts_service.py` |
| CSS Apple Books | `assets/css/style.css` | `app/styles/` |

---

### 2. Récupérer les patterns fonctionnels

**Pattern 1 : Chunking avec overlap**
```python
def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += (chunk_size - overlap)
    return chunks
```

**Pattern 2 : Contextual embeddings**
```python
def contextualize_chunk(self, chunk: str, full_document_context: str) -> str:
    prompt = f"""
    <document>{full_document_context[:10000]}</document>
    <chunk>{chunk}</chunk>
    Please give a short context to situate this chunk...
    """
    # Appel LLM pour contextualiser
```

**Pattern 3 : Découpage par chapitres**
```python
import re
chapter_splits = re.split(r'(^# .+)', md_text, flags=re.MULTILINE)
```

---

### 3. Ne PAS récupérer

| Élément | Raison |
|---------|--------|
| `app.py` entier | Trop monolithique, tout refaire proprement |
| Structure library_data/ | Incohérente, utiliser notre nouvelle structure |
| Backend FastAPI | Non utilisé, recréer avec bonne architecture |

---

## Plan de migration

### Phase 1 : Extraire les fonctions utiles

```bash
# Copier les fichiers réutilisables
cp _LivreLLM/core/scanner.py → book-reader/src/conversion/
cp _LivreLLM/assets/css/ → book-reader/app/styles/
```

### Phase 2 : Adapter les services

1. `VectorService` → Adapter pour Qdrant Docker + OpenAI embeddings
2. `LLMService` → Garder multi-provider, ajouter Ollama
3. `TTSService` → Garder OpenAI, ajouter OpenAI Realtime

### Phase 3 : Réutiliser les patterns

- Chunking avec overlap
- Contextual embeddings
- Découpage chapitres regex
- CSS Apple Books

---

## Valeur récupérable

| Élément | Valeur | Effort adaptation |
|---------|--------|-------------------|
| `scanner.py` | 🟢 Haute | Faible |
| CSS Apple Books | 🟢 Haute | Faible |
| Patterns chunking | 🟢 Haute | Aucun |
| VectorService | 🟡 Moyenne | Moyen (changer embeddings) |
| LLMService | 🟡 Moyenne | Moyen (ajouter distillation) |
| app.py | 🔴 Faible | Tout refaire |

---

## Conclusion

Le projet existant a validé les concepts :
- ✅ Marker fonctionne pour PDF → Markdown
- ✅ Qdrant + FastEmbed fonctionne localement
- ✅ OpenAI TTS fonctionne
- ✅ Chat RAG fonctionne
- ✅ Interface Apple Books est esthétique

**Mais** la structure est à refaire complètement selon notre nouvelle architecture.
