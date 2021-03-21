from fastapi import APIRouter

from nsetools import Nse
from urllib.error import HTTPError

nse = Nse()
nse_router = APIRouter()

# Common Routes
@nse_router.get("/lotsizes")
async def get_lot_sizes():
    try:
        lot_sizes = nse.get_fno_lot_sizes()
        return {"success": True,"lot_sizes": lot_sizes }
    except HTTPError:
        return {"success": False, "message": "Not Found"} 


# Index routes
@nse_router.get("/indices")
async def get_indices():
    try:
        indices = nse.get_index_list()
        return {"success": True,"indices": indices }
    except HTTPError:
        return {"success": False, "message": "Not Found"} 

@nse_router.get("/index/{index}/quote")
async def get_index_quote(index: str):
    try:
        quote = nse.get_index_quote(index)
        return {"success": True,"quote": quote}
    except HTTPError:
        return {"success": False, "message": "Not Found"} 

@nse_router.get("/index/advances/declines")
async def get_advances_declines():
    try:
        advances_declines = nse.get_advances_declines()
        return {"success": True,"advances_declines": advances_declines }
    except HTTPError:
        return {"success": False, "message": "Not Found"} 

@nse_router.get("/index/{stock}/validate")
async def is_valid_index(stock: str):
    try:
        is_valid = nse.is_valid_index(stock)
        return {"success": True,"valid": is_valid }
    except HTTPError:
        return {"success": False, "message": "Not Found"} 



# Stock Routes
@nse_router.get("/stock/{stock}/quote")
async def get_stock_quote(stock: str):
    try:
        quote = nse.get_quote(stock)
        return {"success": True,"quote": quote}
    except HTTPError:
        return {"success": False, "message": "Not Found"} 

@nse_router.get("/stock/codes")
async def get_stock_codes():
    try:
        stock_codes = nse.get_stock_codes()
        return {"success": True,"codes": stock_codes }
    except HTTPError:
        return {"success": False, "message": "Not Found"} 

@nse_router.get("/stocks/activity")
async def get_gainers_and_losers():
    try:
        top_gainers = nse.get_top_gainers()
        return {"success": True,"activity": top_gainers }
    except HTTPError:
        return {"success": False, "message": "Not Found"} 

@nse_router.get("/stock/{stock}/validate")
async def is_valid_stock(stock: str):
    try:
        is_valid = nse.is_valid_code(stock)
        return {"success": True,"valid": is_valid }
    except HTTPError:
        return {"success": False, "message": "Not Found"} 
