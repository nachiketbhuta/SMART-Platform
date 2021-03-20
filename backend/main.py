from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.nse import nse_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://smart-platform-hacknitr.herokuapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(nse_router, prefix="/nse", tags=["nse"])

@app.get("/")
def index():
    return {"msg": "Hello World"}
