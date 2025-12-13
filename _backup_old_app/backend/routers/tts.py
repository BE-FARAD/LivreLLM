from fastapi import APIRouter, HTTPException, Response
from pydantic import BaseModel
from openai import OpenAI
import os

router = APIRouter(prefix="/tts", tags=["tts"])
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class TTSRequest(BaseModel):
    text: str

@router.post("/")
async def generate_speech(request: TTSRequest):
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=request.text
        )
        return Response(content=response.content, media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
