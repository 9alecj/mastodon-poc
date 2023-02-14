from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import TimelineRouter, TrendsRouter

app = FastAPI()

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

timelineRouter = TimelineRouter()
trendsRouter = TrendsRouter()

app.include_router(timelineRouter.router)
app.include_router(trendsRouter.router)


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
