from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

from backend.routers import books, chat, tts, livekit_token

app = FastAPI(title="LivreLLM Backend")

# Configure CORS - Must be added before other middleware/routers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router)
app.include_router(chat.router)
app.include_router(tts.router)
app.include_router(livekit_token.router)
from backend.routers import ingest
app.include_router(ingest.router)

@app.get("/")
async def root():
    return {"message": "LivreLLM Backend is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
