from fastapi import APIRouter
from src.services import PostsService

class PostsRouter():
    def __init__(self):
        self.posts_service = PostsService()
        self.router = APIRouter(prefix="/posts")
        self.router.add_api_route("/", self.get_public_timeline, tags=["public"], methods=["GET"])
        self.router.add_api_route("/trending", self.get_trending_statuses, tags=["public"], methods=["GET"])
        self.router.add_api_route("/tag", self.get_public_timeline_by_tag, tags=["public"], methods=["GET"])

    async def get_public_timeline(self):
        return await self.posts_service.get_public_posts()
    
    async def get_trending_statuses(self):
        return await self.posts_service.get_trending_posts()

    async def get_public_timeline_by_tag(self, tag: str):
        return await self.posts_service.get_posts_by_tag(tag)
