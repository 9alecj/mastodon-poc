from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # NEW
from src.routers import public_endpoints


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

app.include_router(public_endpoints.router)


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
