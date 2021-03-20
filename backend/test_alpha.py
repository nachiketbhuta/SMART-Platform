from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_series_data():
    response = client.get("/alpha/timeseries/SBI/time_series_daily")
    assert response.status_code == 200

def test_fundamental_data():
    response = client.get("/alpha/fundamentals/SBI/overview")
    assert response.status_code == 200
