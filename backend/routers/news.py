from fastapi import APIRouter
import finviz

news_router = APIRouter()

@news_router.get("/{stock}/news")
async def get_stock_news(stock: str):
    news = finviz.get_news(stock)
    return {"news": news[0:5]}
