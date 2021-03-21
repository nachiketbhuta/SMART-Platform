from fastapi import APIRouter
import finviz

news_router = APIRouter()

@news_router.get("/{stock}/news")
async def get_stock_news(stock: str):
    try:
        news = finviz.get_news(stock)
        return {"success": True, "news": news[0:5]}
    except HTTPError:
        return {"success": False, "message": "Not Found"} 
