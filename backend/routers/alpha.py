from fastapi import APIRouter
import os
import requests

from dotenv import load_dotenv

load_dotenv()
alpha_vantage_router = APIRouter()
API_KEY = os.getenv("API_KEY")

def create_url(function, symbol, is_series):
    function = function.upper()
    url = ""
    if is_series:
        url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={API_KEY}&interval=5min&outputsize=full'
    else:
        url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={API_KEY}'
    return url

def get_data(function, symbol, is_series):
    url = create_url(function, symbol, is_series)
    response = requests.get(url)
    # print(response.json())
    return response.json()


@alpha_vantage_router.get("/fundamentals/{symbol}/{function}")
async def get_fundamental_data(symbol: str, function: str):
    response = get_data(function, symbol, False)
    return response

@alpha_vantage_router.get("/timeseries/{symbol}/{function}")
async def get_series_data(symbol: str, function: str):
    response = get_data(function, symbol, True)
    return response