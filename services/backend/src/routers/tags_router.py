from fastapi import APIRouter

from src.services import TagsService

class TagsRouter():
    def __init__(self):
        self.tags_service = TagsService()
        self.router = APIRouter(prefix='/tags')

        self.router.add_api_route("/", self.get_trending_tags, tags=["public"], methods=["GET"])

    async def get_trending_tags(self):
        return await self.tags_service.get_trending_tags()
