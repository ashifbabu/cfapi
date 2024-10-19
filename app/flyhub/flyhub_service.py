from .flyhub_utils import get_flyhub_token
from app.utils import call_external_api  # Importing from utils.py now

async def flyhub_flight_search(origin, destination, date):
    token = await get_flyhub_token()
    payload = {
        "AdultQuantity": 1,
        "JourneyType": "1",
        "Segments": [{
            "Origin": origin,
            "Destination": destination,
            "DepartureDateTime": date
        }]
    }
    url = "https://api.flyhub.com/api/v1/AirSearch"
    headers = {"Authorization": f"Bearer {token}"}
    return await call_external_api(url, payload)
