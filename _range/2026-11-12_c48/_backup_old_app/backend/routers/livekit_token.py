from fastapi import APIRouter, HTTPException
from livekit import api
import os
import uuid

router = APIRouter(prefix="/livekit", tags=["livekit"])

@router.get("/token")
async def get_token(participant_name: str = "User"):
    api_key = os.getenv("LIVEKIT_API_KEY")
    api_secret = os.getenv("LIVEKIT_API_SECRET")
    livekit_url = os.getenv("LIVEKIT_URL")

    if not api_key or not api_secret:
        raise HTTPException(status_code=500, detail="LiveKit credentials not configured")

    # Create Access Token
    token = api.AccessToken(api_key, api_secret) \
        .with_identity(f"user-{uuid.uuid4()}") \
        .with_name(participant_name) \
        .with_grants(api.VideoGrants(room_join=True, room="chat-room"))
    
    return {"token": token.to_jwt(), "url": livekit_url}
