#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Test OpenAI Connection
print("=" * 50)
print("TEST 1: Connexion OpenAI")
print("=" * 50)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print("✅ Client OpenAI initialisé")

# Test Transcription
print("\n" + "=" * 50)
print("TEST 2: Transcription Audio")
print("=" * 50)

with open("test_audio.wav", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        language="fr"
    )
    print(f"✅ Transcription réussie: '{transcript.text}'")

# Test LLM
print("\n" + "=" * 50)
print("TEST 3: LLM Response")
print("=" * 50)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Dis bonjour en une phrase"}]
)
print(f"✅ LLM Response: '{response.choices[0].message.content}'")

# Test TTS
print("\n" + "=" * 50)
print("TEST 4: Text-to-Speech")
print("=" * 50)

tts_response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Ceci est un test"
)
with open("test_output.mp3", "wb") as f:
    f.write(tts_response.content)
print(f"✅ TTS généré: test_output.mp3 ({len(tts_response.content)} bytes)")

print("\n" + "=" * 50)
print("TOUS LES TESTS ONT RÉUSSI!")
print("=" * 50)
