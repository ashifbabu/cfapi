from app.bdfare.bdfare_service import bdfare_flight_search

async def test_bdfare_search():
    response = await bdfare_flight_search("DEL", "DXB", "2024-10-15")
    assert response["Results"] is not None
