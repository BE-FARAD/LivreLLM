import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    # LLM
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")

    # TTS
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
