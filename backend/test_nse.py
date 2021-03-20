from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_index_quote():
    response = client.get("/nse/index/NIFTY/quote")
    assert response.status_code == 200

def test_get_indices():
    response = client.get("/nse/indices")
    assert response.status_code == 200

def test_lot_sizes():
    response = client.get("/nse/lotsizes")
    assert response.status_code == 200

def test_advances_declines():
    response = client.get("/nse/index/advances/declines")
    assert response.status_code == 200

def test_valid_index():
    response = client.get("/nse/index/SBI/validate")
    assert response.status_code == 200

def test_stock_quote():
    response = client.get("/nse/stock/SBI/quote")
    assert response.status_code == 200

def test_stock_codes():
    response = client.get("/nse/stock/codes")
    assert response.status_code == 200

def test_gainers_and_losers():
    response = client.get("/nse/stocks/activity")
    assert response.status_code == 200

def test_valid_stock():
    response = client.get("/nse/stock/SBI/validate")
    assert response.status_code == 200