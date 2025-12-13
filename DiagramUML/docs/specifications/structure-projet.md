# Structure du Projet Python

> Application de Lecture Interactive de Livres Techniques

## Arborescence du projet

```
book-reader/
├── .env                          # Variables d'environnement (API keys)
├── .env.example                  # Template des variables d'environnement
├── .gitignore                    # Fichiers à ignorer
├── pyproject.toml                # Configuration uv/projet
├── README.md                     # Documentation du projet
│
├── app/                          # Application Streamlit
│   ├── __init__.py
│   ├── main.py                   # Point d'entrée Streamlit
│   ├── pages/                    # Pages Streamlit
│   │   ├── __init__.py
│   │   ├── home.py               # Page d'accueil
│   │   ├── library.py            # Bibliothèque de livres
│   │   ├── reader.py             # Lecteur de chapitres
│   │   ├── settings.py           # Paramètres utilisateur
│   │   └── import_book.py        # Import de nouveaux livres
│   ├── components/               # Composants UI réutilisables
│   │   ├── __init__.py
│   │   ├── audio_player.py       # Lecteur audio HTML5
│   │   ├── chapter_selector.py   # Sélecteur de chapitres
│   │   ├── chat_interface.py     # Interface de chat Q&A
│   │   └── memory_card_view.py   # Affichage des fiches mémoire
│   └── styles/                   # CSS personnalisé
│       └── main.css
│
├── src/                          # Code source principal
│   ├── __init__.py
│   │
│   ├── input/                    # Package Input
│   │   ├── __init__.py
│   │   └── file_watcher.py       # FileWatcher
│   │
│   ├── conversion/               # Package Conversion
│   │   ├── __init__.py
│   │   ├── marker_converter.py   # MarkerConverter
│   │   ├── markdown_document.py  # MarkdownDocument
│   │   ├── chapter.py            # Chapter
│   │   └── paragraph.py          # Paragraph
│   │
│   ├── storage/                  # Package Storage
│   │   ├── __init__.py
│   │   ├── image_manager.py      # ImageManager
│   │   ├── audio_manager.py      # AudioManager
│   │   └── tts_service.py        # TTSService (OpenAI Realtime)
│   │
│   ├── vectorization/            # Package Vectorization
│   │   ├── __init__.py
│   │   ├── text_chunker.py       # TextChunker
│   │   ├── embedding_service.py  # EmbeddingService
│   │   ├── qdrant_client.py      # QdrantClient
│   │   └── vector_store.py       # VectorStore
│   │
│   ├── translation/              # Package Translation
│   │   ├── __init__.py
│   │   ├── translation_service.py # TranslationService
│   │   └── document_manager.py   # DocumentManager
│   │
│   ├── llm/                      # Package LLM
│   │   ├── __init__.py
│   │   ├── llm_client.py         # LLMClient (OpenAI + Ollama)
│   │   ├── rag_engine.py         # RAGEngine
│   │   └── distillation_service.py # DistillationService
│   │
│   ├── reading/                  # Package ReadingSession
│   │   ├── __init__.py
│   │   ├── reading_session_manager.py # ReadingSessionManager
│   │   ├── memory_card_generator.py   # MemoryCardGenerator
│   │   └── memory_card.py        # MemoryCard
│   │
│   ├── user/                     # Package UserSession
│   │   ├── __init__.py
│   │   ├── user.py               # User
│   │   ├── user_preferences.py   # UserPreferences
│   │   ├── session_persistence.py # SessionPersistence
│   │   ├── reading_state.py      # ReadingState
│   │   └── app_settings.py       # AppSettings
│   │
│   └── orchestration/            # Package Orchestration
│       ├── __init__.py
│       ├── pipeline.py           # Pipeline
│       └── application_controller.py # ApplicationController
│
├── data/                         # Données de l'application
│   ├── 01-input/                 # Dépôt des PDF
│   │   └── .gitkeep
│   ├── 02-output/                # Documents Markdown
│   │   └── .gitkeep
│   ├── images/                   # Images extraites
│   │   └── .gitkeep
│   ├── audio/                    # Fichiers audio TTS
│   │   └── .gitkeep
│   ├── memory_cards/             # Fiches mémoire
│   │   └── .gitkeep
│   └── sessions/                 # Sessions utilisateur (JSON)
│       └── .gitkeep
│
├── config/                       # Configuration
│   ├── __init__.py
│   ├── settings.py               # Chargement des settings
│   └── prompts/                  # Templates de prompts LLM
│       ├── summarize.txt
│       ├── translate.txt
│       ├── distill_formula.txt
│       ├── distill_code.txt
│       └── rag_query.txt
│
├── tests/                        # Tests
│   ├── __init__.py
│   ├── test_file_watcher.py
│   ├── test_marker_converter.py
│   ├── test_vector_store.py
│   └── ...
│
└── scripts/                      # Scripts utilitaires
    ├── setup_qdrant.py           # Initialisation Qdrant
    └── migrate_data.py           # Migration de données
```

## Fichiers de configuration

### pyproject.toml

```toml
[project]
name = "book-reader"
version = "0.1.0"
description = "Application de lecture interactive de livres techniques"
requires-python = ">=3.12"
dependencies = [
    # Core
    "streamlit>=1.28.0",
    "python-dotenv>=1.0.0",

    # PDF Conversion
    "marker-pdf>=0.2.0",

    # LLM
    "openai>=1.0.0",
    "ollama>=0.1.0",

    # Vector Store
    "qdrant-client>=1.6.0",

    # Audio
    "pydub>=0.25.0",

    # Utils
    "pydantic>=2.0.0",
    "httpx>=0.25.0",
    "langdetect>=1.0.9",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "ruff>=0.1.0",
]

[tool.uv]
dev-dependencies = [
    "pytest>=7.0.0",
    "ruff>=0.1.0",
]

[tool.ruff]
line-length = 100
target-version = "py312"
```

### .env.example

```env
# LLM Configuration
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...
LLM_MODEL=gpt-4o-mini

# Ollama (alternative)
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3

# TTS Configuration
TTS_PROVIDER=openai_realtime
TTS_VOICE=alloy
TTS_FORMAT=mp3
TTS_QUALITY=standard

# Embeddings
EMBEDDING_MODEL=text-embedding-3-small

# Qdrant
QDRANT_HOST=localhost
QDRANT_PORT=6333

# Application
APP_PORT=8501
DEBUG=false
```

### .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
.venv/
venv/

# Environment
.env

# Data (garder la structure, pas les fichiers)
data/01-input/*.pdf
data/02-output/*
data/images/*
data/audio/*
data/memory_cards/*
data/sessions/*
!data/**/.gitkeep

# IDE
.idea/
.vscode/
*.swp

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/
```

## Commandes de démarrage

```bash
# 1. Créer le projet avec uv
uv init book-reader
cd book-reader

# 2. Installer les dépendances
uv sync

# 3. Copier la configuration
cp .env.example .env
# Éditer .env avec vos API keys

# 4. Lancer Qdrant (Docker)
docker run -p 6333:6333 qdrant/qdrant

# 5. Lancer l'application
uv run streamlit run app/main.py
```

## Ordre de développement recommandé

### Phase 1 : Infrastructure de base
1. [ ] Configuration (config/, .env)
2. [ ] FileWatcher (src/input/)
3. [ ] MarkerConverter (src/conversion/)
4. [ ] ImageManager (src/storage/)
5. [ ] DocumentManager (src/translation/)

### Phase 2 : Vectorisation et LLM
6. [ ] QdrantClient (src/vectorization/)
7. [ ] EmbeddingService (src/vectorization/)
8. [ ] VectorStore (src/vectorization/)
9. [ ] LLMClient (src/llm/)
10. [ ] TranslationService (src/translation/)

### Phase 3 : Audio et Distillation
11. [ ] TTSService (src/storage/)
12. [ ] DistillationService (src/llm/)
13. [ ] AudioManager (src/storage/)

### Phase 4 : Session de lecture
14. [ ] User & UserPreferences (src/user/)
15. [ ] SessionPersistence (src/user/)
16. [ ] ReadingSessionManager (src/reading/)
17. [ ] RAGEngine (src/llm/)
18. [ ] MemoryCardGenerator (src/reading/)

### Phase 5 : Interface Streamlit
19. [ ] Page Settings (app/pages/)
20. [ ] Page Import (app/pages/)
21. [ ] Page Library (app/pages/)
22. [ ] Page Reader (app/pages/)
23. [ ] Composants UI (app/components/)

### Phase 6 : Orchestration
24. [ ] Pipeline (src/orchestration/)
25. [ ] ApplicationController (src/orchestration/)
26. [ ] Tests

## Dépendances Docker

### docker-compose.yml (optionnel)

```yaml
version: '3.8'

services:
  qdrant:
    image: qdrant/qdrant:latest
    ports:
      - "6333:6333"
    volumes:
      - qdrant_data:/qdrant/storage

volumes:
  qdrant_data:
```
