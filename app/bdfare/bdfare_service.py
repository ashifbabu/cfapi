from app.utils import call_external_api  # Importing from utils.py now

async def bdfare_flight_search(origin, destination, date):
    payload = {
        "origin": origin,
        "destination": destination,
        "departureDate": date
    }
    url = "https://bdfare.com/api/enterprise/AirShopping"
    return await call_external_api(url, payload)
