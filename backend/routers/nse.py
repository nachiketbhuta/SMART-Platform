from fastapi import APIRouter

from nsetools import Nse

nse = Nse()
nse_router = APIRouter()

# Common Routes
@nse_router.get("/lotsizes")
async def get_lot_sizes():
    lot_sizes = nse.get_fno_lot_sizes()
    return {"lot_sizes": lot_sizes }


# Index routes
@nse_router.get("/indices")
async def get_indices():
    indices = nse.get_index_list()
    return {"indices": indices }

@nse_router.get("/index/{index}/quote")
async def get_index_quote(index: str):
    quote = nse.get_index_quote(index)
    return {"quote": quote}

@nse_router.get("/index/advances/declines")
async def get_advances_declines():
    advances_declines = nse.get_advances_declines()
    return {"advances_declines": advances_declines }

@nse_router.get("/index/{stock}/validate")
async def is_valid_index(stock: str):
    is_valid = nse.is_valid_index(stock)
    return {"valid": is_valid }



# Stock Routes
@nse_router.get("/stock/{stock}/quote")
async def get_stock_quote(stock: str):
    quote = nse.get_quote(stock)
    return {"quote": quote}

@nse_router.get("/stock/codes")
async def get_stock_codes():
    stock_codes = nse.get_stock_codes()
    return {"codes": stock_codes }

@nse_router.get("/stocks/activity")
async def get_gainers_and_losers():
    top_gainers = nse.get_top_gainers()
    return {"activity": top_gainers }

@nse_router.get("/stock/{stock}/validate")
async def is_valid_stock(stock: str):
    is_valid = nse.is_valid_code(stock)
    return {"valid": is_valid }
