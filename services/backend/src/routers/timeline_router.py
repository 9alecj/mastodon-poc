from fastapi import APIRouter

from src.services import TimelineService

class TimelineRouter():
    def __init__(self):
        self.timeline_service = TimelineService()
        self.router = APIRouter()
        self.router.add_api_route("/timelines", self.get_public_timeline, tags=["public"], methods=["GET"])
        self.router.add_api_route("/timelines/tag", self.get_public_timeline_by_tag, tags=["public"], methods=["GET"])

    async def get_public_timeline(self):
        return await self.timeline_service.fetch_timeline()

    async def get_public_timeline_by_tag(self, tag: str):
        return await self.timeline_service.fetch_timeline_by_tag(tag)
