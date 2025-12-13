from openai import OpenAI
from config.settings import settings

class LLMClient:
    """Unified Client for LLM interactions."""
    
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.LLM_MODEL

    def chat(self, messages: list) -> str:
        """Simple chat completion."""
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"

    def translate(self, text: str, target_lang: str = "fr") -> str:
        """Specialized translation method."""
        prompt = f"Translate the following technical text to {target_lang}. Preserve markdown formatting, code blocks, and math formulas exactly. Text:\n\n{text}"
        return self.chat([
            {"role": "system", "content": "You are a professional technical translator."},
            {"role": "user", "content": prompt}
        ])
