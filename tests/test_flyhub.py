from app.flyhub.flyhub_service import flyhub_flight_search

async def test_flyhub_search():
    response = await flyhub_flight_search("DEL", "DXB", "2024-10-15")
    assert response["Results"] is not None
