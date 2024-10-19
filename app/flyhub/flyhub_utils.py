import httpx
from app.config import settings

async def get_flyhub_token():
    payload = {
        "username": settings.FLYHUB_USERNAME,
        "apikey": settings.FLYHUB_API_KEY
    }
    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.flyhub.com/api/v1/Authenticate", json=payload)
        response.raise_for_status()
        return response.json().get("TokenId")
