from openai import OpenAI
from config.settings import settings

class TTSService:
    """Text-to-Speech Service using OpenAI."""
    
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.voice = settings.TTS_VOICE
        self.model = "tts-1"

    def generate_audio(self, text: str) -> bytes:
        """Generates audio bytes from text."""
        try:
            response = self.client.audio.speech.create(
                model=self.model,
                voice=self.voice,
                input=text
            )
            return response.content
        except Exception as e:
            print(f"TTS Error: {e}")
            return None
