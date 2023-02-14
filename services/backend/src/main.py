from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import PostsRouter, TagsRouter , LinksRouter

app = FastAPI()

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

posts_router = PostsRouter()
links_router = LinksRouter()
tags_router = TagsRouter()

app.include_router(posts_router.router)
app.include_router(links_router.router)
app.include_router(tags_router.router)


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
