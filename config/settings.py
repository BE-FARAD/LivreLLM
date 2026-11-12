import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    # LLM — le defaut est **local** depuis la phase 0 de C48 (decision 4 d'AF) :
    # aucun contenu de norme, de Techniques de l'Ingenieur ou de piece client ne
    # part vers un service externe. Un fournisseur distant se nomme
    # explicitement, poste par poste, dans le `.env` : il ne s'obtient jamais en
    # ne reglant rien.
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")

    # TTS — la synthese vocale n'a pas d'equivalent local dans ce depot
    # aujourd'hui : `src/livrellm/storage/tts_service.py` appelle OpenAI, et
    # rien d'autre. Le defaut reste donc `openai`, **et c'est une limite a
    # connaitre** : un texte lu a voix haute part vers un service externe. Le
    # chemin local reste a ecrire ; tant qu'il n'existe pas, on ne fait pas
    # semblant qu'il existe en ecrivant un defaut qui ne marcherait pas.
    TTS_PROVIDER = os.getenv("TTS_PROVIDER", "openai")
    TTS_VOICE = os.getenv("TTS_VOICE", "alloy")
    TTS_FORMAT = os.getenv("TTS_FORMAT", "mp3")
    TTS_QUALITY = os.getenv("TTS_QUALITY", "standard")

    # Embeddings
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

    # Qdrant
    QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT = int(os.getenv("QDRANT_PORT", "6333"))

    # App
    APP_PORT = int(os.getenv("APP_PORT", "8501"))
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    
    # Paths
    BASE_DIR = Path(__file__).parent.parent
    DATA_DIR = BASE_DIR / "data"
    INPUT_DIR = DATA_DIR / "01-input"
    OUTPUT_DIR = DATA_DIR / "02-output"
    IMAGES_DIR = DATA_DIR / "images"
    AUDIO_DIR = DATA_DIR / "audio"
    MEMORY_CARDS_DIR = DATA_DIR / "memory_cards"
    SESSIONS_DIR = DATA_DIR / "sessions"

    @classmethod
    def validate(cls):
        if cls.LLM_PROVIDER == "openai" and not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required for OpenAI provider")

settings = Settings()
