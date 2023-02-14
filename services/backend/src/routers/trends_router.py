from fastapi import APIRouter

from src.services import TrendsService

class TrendsRouter():
    def __init__(self):
        self.trends_service = TrendsService()
        self.router = APIRouter()
        self.router.add_api_route("/trending-statuses", self.get_trending_statuses, tags=["public"], methods=["GET"])
        self.router.add_api_route("/trending-links", self.get_trending_links, tags=["public"], methods=["GET"])
        self.router.add_api_route("/trends", self.get_trends, tags=["public"], methods=["GET"])

    async def get_trending_statuses(self):
        return await self.trends_service.fetch_trending_statuses()

    async def get_trending_links(self):
        return await self.trends_service.fetch_trending_links()

    async def get_trends(self):
        return await self.trends_service.fetch_trends()
