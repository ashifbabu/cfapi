from app.utils import combined_flight_search

async def test_combined_search():
    response = await combined_flight_search("DEL", "DXB", "2024-10-15")
    assert response["flyhub"] is not None
    assert response["bdfare"] is not None

