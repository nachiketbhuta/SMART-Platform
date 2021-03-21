from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.nse import nse_router
from routers.alpha import alpha_vantage_router
from routers.news import news_router
from routers.tweets import tweets_router

app = FastAPI()

origins = [
    "http://localhost",
    "https://smart-platform-hacknitr.herokuapp.com",
    "http://smart-platform-hacknitr.herokuapp.com",
    "http://localhost:8081",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(nse_router, prefix="/nse", tags=["nse"])
app.include_router(alpha_vantage_router, prefix="/alpha", tags=["alpha"])
app.include_router(news_router, prefix="/news", tags=["news"])
app.include_router(tweets_router, prefix="/tweets", tags=["tweets"])



@app.get("/")
def index():
    return {"msg": "Hello World"}
