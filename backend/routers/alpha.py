import os

import requests
from dotenv import load_dotenv
from fastapi import APIRouter

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


@alpha_vantage_router.get("/search/{keywords}")
async def get_search_results(keywords: str):
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keywords}&apikey={API_KEY}'
    response = requests.get(url)
    return response.json()


@alpha_vantage_router.get("/indicators/{symbol}/{function}/{interval}/{time_period}/{series_type}")
async def get_sma_ema_rsi_data(symbol: str, function: str, interval: str, time_period: str, series_type: str):
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}'
    response = requests.get(url)
    return response.json()


@alpha_vantage_router.get("/indicators/{symbol}/{function}/{interval}")
async def get_stoch_obv_data(symbol: str, function: str, interval: str):
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&apikey={API_KEY}'
    response = requests.get(url)
    return response.json()


@alpha_vantage_router.get("/indicators/{symbol}/{function}/{interval}/{time_period}")
async def get_adx_cci_data(symbol: str, function: str, interval: str, time_period: str):
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&apikey={API_KEY}'
    response = requests.get(url)
    return response.json()
