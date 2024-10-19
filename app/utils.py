import httpx
from tenacity import retry, wait_exponential, stop_after_attempt

@retry(wait=wait_exponential(multiplier=1, min=2), stop=stop_after_attempt(3))
async def call_external_api(url, payload):
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(url, json=payload)
        response.raise_for_status()
        return response.json()

from .flyhub.flyhub_service import flyhub_flight_search
from .bdfare.bdfare_service import bdfare_flight_search

async def combined_flight_search(origin: str, destination: str, date: str):
    flyhub_results = await flyhub_flight_search(origin, destination, date)
    bdfare_results = await bdfare_flight_search(origin, destination, date)
    return {
        "flyhub": flyhub_results.get("Results", []),
        "bdfare": bdfare_results.get("Results", [])
    }
