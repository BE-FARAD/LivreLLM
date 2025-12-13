# Décisions Techniques - Application Lecture Interactive

> Remplissez ce fichier avant de lancer la programmation.
> Cochez les options choisies avec `[x]` et complétez les valeurs.

---

## 1. LLM - Modèle de langage

### Quel LLM utiliser ?

- [x] OpenAI GPT-4 / GPT-4o mini
- [ ] OpenAI GPT-3.5-turbo
- [ ] Anthropic Claude (Sonnet / Opus)
- [ ] Mistral (API)
- [x] Ollama (local) - Modèle : _______________
- [ ] Autre : _______________

### Configuration

| Paramètre | Valeur |
|-----------|--------|
| API Key (variable env) | `_oui______________` |
| Temperature | `0,0` (ex: 0.7) |
| Max tokens | `____selon le model__` (ex: 4096) |
| Streaming activé | [ ] Oui  [ ] Non |

---

## 2. TTS - Synthèse vocale

### Quelle API TTS ?

- [x] OpenAI realTime (`tts-1` / `tts-1-hd`)
- [ ] ElevenLabs
- [ ] Google Cloud Text-to-Speech
- [ ] Azure Cognitive Services
- [ ] Coqui TTS (local, gratuit)
- [ ] Piper (local, gratuit)
- [ ] Autre : _______________

### Configuration

| Paramètre | Valeur |
|-----------|--------|
| Voix française | `donne le choix à l'utilisateur _` (ex: "alloy", "nova") | menu parametre pour les reglages: sombre, clair, voix homme, femme etc
| Format audio | [x] MP3  [ ] WAV  [ ] OGG |
| Qualité | [x] Standard  [ ] HD |

### Traitement des éléments spéciaux

**Formules mathématiques :**
- [ ] Ignorer (ne pas lire)
- [x] Lire en texte (ex: "E égale m c carré") distillation des équations + analogie
- [ ] Signal sonore pour indiquer une formule
- [ ] Autre : _______________

**Blocs de code :**
- [ ] Ignorer (ne pas lire)
- [x] Lire le code distillation + analogie
- [ ] Signal sonore pour indiquer du code
- [ ] Dire "bloc de code" et passer
- [ ] Autre : _______________

---

## 3. Embeddings - Vectorisation

### Quel modèle d'embedding ?

- [x] OpenAI `text-embedding-3-small` (1536 dim)
- [x] OpenAI `text-embedding-3-large` (3072 dim)
- [ ] OpenAI `text-embedding-ada-002` (1536 dim)
- [ ] Sentence-Transformers `all-MiniLM-L6-v2` (384 dim, local)
- [ ] Sentence-Transformers `paraphrase-multilingual-MiniLM-L12-v2` (384 dim, local, multilingue)
- [ ] Cohere `embed-multilingual-v3.0`
- [ ] Autre : ______cré un fichier parametre pour donner le choix à l'utilisateur selon l'importance du livre et reduire les coût_________

### Configuration chunking

| Paramètre | Valeur |
|-----------|--------|
| Taille des chunks | `_______________` tokens (ex: 1000) |
| Overlap entre chunks | `_______________` tokens (ex: 100) |
| Stratégie de découpage | [ ] Par paragraphe  [ ] Par taille fixe  [x] Par section |
 voir la méthode claude contexte
---

## 4. Qdrant - Base vectorielle

### Déploiement

- [x] Local avec Docker
- [ ] Local sans Docker (binaire)
- [ ] Qdrant Cloud (hébergé)

### Configuration

| Paramètre | Valeur |
|-----------|--------|
| Host | `_______________` (ex: localhost) |
| Port | `_______________` (ex: 6333) |
| API Key (si cloud) | `_______________` |

### Organisation des collections

- [x] Une collection par livre (ex: `book_clean_code`)
- [ ] Une collection globale avec filtres par livre (ex: `books`)

---

## 5. Authentification utilisateur

### Type d'authentification

- [x] Simple (username local, sans mot de passe)
- [ ] Username + mot de passe (hashé)
- [ ] OAuth Google
- [ ] OAuth GitHub
- [ ] Pas d'authentification (mono-utilisateur)

### Stockage des sessions

- [x] Fichiers JSON (`sessions/{userId}/`)
- [ ] SQLite
- [ ] Redis
- [ ] PostgreSQL

---

## 6. Marker - Conversion PDF

### Configuration

| Paramètre | Valeur |
|-----------|--------|
| GPU activé | [ ] Oui  [x] Non (CPU only) |
| OCR activé | [ ] Oui  [ ] Non |
| Langue OCR | `_______________` (ex: fra, eng, fra+eng) |
| Batch size | `_______________` (ex: 4) |

### Extraction

- [x] Images (activé par défaut)
- [x] Tableaux (activé par défaut)
- [x] Formules LaTeX (activé par défaut)
- [x] code de programmation (activé par défaut)

---

## 7. Structure du projet Python

### Gestionnaire de dépendances

- [ ] Poetry
- [ ] pip + requirements.txt
- [x] uv
- [ ] conda

### Version Python

- [ ] Python 3.10
- [ ] Python 3.11
- [x] Python 3.12

### Framework de tests

- [ ] pytest
- [ ] unittest
- [ ] Pas de tests (déconseillé)

### Linter / Formatter

- [ ] Ruff
- [ ] Black + Flake8
- [ ] Aucun

---

## 8. Interface Streamlit

### Configuration

| Paramètre | Valeur |
|-----------|--------|
| Port | `_______________` (ex: 8501) |
| Thème | [ ] Light  [ ] Dark  [ ] Auto |

### Fonctionnalités audio

- [x] Lecteur audio intégré (HTML5)
- [x] Contrôles play/pause/seek
- [x] Affichage progression

---

## 9. Variables d'environnement

> Liste des variables à configurer dans un fichier `.env`

```env
# LLM
LLM_PROVIDER=_______________
LLM_API_KEY=_______________
LLM_MODEL=_______________

# TTS
TTS_PROVIDER=_______________
TTS_API_KEY=_______________
TTS_VOICE=_______________

# Embeddings
EMBEDDING_PROVIDER=_______________
EMBEDDING_API_KEY=_______________
EMBEDDING_MODEL=_______________

# Qdrant
QDRANT_HOST=_______________
QDRANT_PORT=_______________
QDRANT_API_KEY=_______________

# Application
APP_PORT=8501
DEBUG=false
```

---

## 10. Estimation des coûts (si APIs payantes)

| Service | Coût estimé |
|---------|-------------|
| LLM (par livre) | $___ |
| TTS (par livre) | $___ |
| Embeddings (par livre) | $___ |
| Qdrant Cloud (mensuel) | $___ |
| **Total par livre** | $___ |

---

## Résumé des choix

| Composant | Choix |
|-----------|-------|
| LLM | OpenAI GPT-4o mini + Ollama (local) |
| TTS | OpenAI Realtime (MP3, Standard, voix configurable) |
| Embeddings | OpenAI text-embedding-3-small/large (choix utilisateur) |
| Qdrant | Local Docker, 1 collection par livre |
| Auth | Simple (username), sessions JSON |
| Python | 3.12 |
| Gestionnaire | uv |

### Fonctionnalités spéciales identifiées

- **Distillation + Analogie** : Pour les formules mathématiques et le code
- **Menu Paramètres** : Thème (sombre/clair), Voix (homme/femme), Modèle embedding
- **Chunking** : Par section (méthode Claude contexte)

---

## Notes et remarques

> Ajoutez ici vos notes ou contraintes spécifiques.

```
_____________________________________________________________________
_____________________________________________________________________
_____________________________________________________________________
_____________________________________________________________________
```

---

*Document généré le : 2024-XX-XX*
*Version : 1.0*
