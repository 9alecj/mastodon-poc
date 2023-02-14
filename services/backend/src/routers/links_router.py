from fastapi import APIRouter

from src.services import LinksService

class LinksRouter():
    def __init__(self):
        self.links_service = LinksService()
        self.router = APIRouter(prefix='/links')

        self.router.add_api_route("/", self.get_trending_links, tags=["public"], methods=["GET"])

    async def get_trending_links(self):
        return await self.links_service.get_trending_links()
