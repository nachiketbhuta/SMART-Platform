from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_news():
    response = client.get("/news/SBI/news")
    assert response.status_code == 200