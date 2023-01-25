from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # NEW
import httpx
import asyncio

public_GET_URL = "https://mastodon.social/api/v1/timelines/public?limit=1"

app = FastAPI()

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    response = httpx.get(public_GET_URL)
    print(response)
    return response.json()