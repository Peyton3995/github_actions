import pytest
from app import app, get_weather

@pytest.fixture()
def client():
    return app.test_client()

def test_index(client):
    weather_data = get_weather()

    response = client.get('wind')
    assert (f'<i>{weather_data[0]["wspd"]}</i>').encode("utf-8") in response.data