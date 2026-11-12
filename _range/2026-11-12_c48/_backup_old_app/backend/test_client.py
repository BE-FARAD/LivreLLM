import asyncio
import os
from livekit import api, rtc
from dotenv import load_dotenv

load_dotenv()

async def test_connection():
    # 1. Generate Token
    token = api.AccessToken(
        os.getenv("LIVEKIT_API_KEY"),
        os.getenv("LIVEKIT_API_SECRET")
    ).with_identity("python-test-user").with_name("Python Test").with_grants(
        api.VideoGrants(room_join=True, room="test-room")
    ).to_jwt()

    url = os.getenv("LIVEKIT_URL")
    print(f"Connecting to {url} with token...")

    # 2. Connect
    room = rtc.Room()
    
    @room.on("connected")
    def on_connected():
        print("✅ CONNECTED to Room!")

    @room.on("disconnected")
    def on_disconnected(reason):
        print(f"❌ DISCONNECTED: {reason}")

    try:
        await room.connect(url, token)
        print("Waiting for connection stability...")
        await asyncio.sleep(5)
        print("Connection stable for 5 seconds.")
        await room.disconnect()
    except Exception as e:
        print(f"❌ FAILED to connect: {e}")

if __name__ == "__main__":
    asyncio.run(test_connection())
