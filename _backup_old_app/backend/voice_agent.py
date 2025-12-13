import logging
import os
from dotenv import load_dotenv
from livekit.agents import JobContext, WorkerOptions, cli, llm, JobRequest
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero

load_dotenv()

logger = logging.getLogger("voice-agent")

async def entrypoint(ctx: JobContext):
    await ctx.connect()
    logger.info("Connected to LiveKit room")

    # Configure Grok via OpenAI plugin
    grok_api_key = os.getenv("GROK_API_KEY")
    grok_url = "https://api.x.ai/v1"
    
    # LLM: Grok
    llm_plugin = openai.LLM(
        api_key=grok_api_key,
        base_url=grok_url,
        model="grok-beta",
    )
    
    # STT: OpenAI Whisper (uses OPENAI_API_KEY from env)
    stt_plugin = openai.STT()
    
    # TTS: Silero (Local, CPU friendly)
    tts_plugin = silero.TTS()
    
    # VAD: Silero
    vad_plugin = silero.VAD.load()
    
    initial_ctx = llm.ChatContext().append(
        role="system",
        text="Tu es un assistant vocal intelligent pour une bibliothèque de livres. Réponds de manière concise et utile en français."
    )
    
    assistant = VoiceAssistant(
        vad=vad_plugin,
        stt=stt_plugin,
        llm=llm_plugin,
        tts=tts_plugin,
        chat_ctx=initial_ctx,
    )
    
    assistant.start(ctx.room)
    
    await assistant.say("Bonjour, je suis prêt à discuter de vos livres.", allow_interruptions=True)

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
