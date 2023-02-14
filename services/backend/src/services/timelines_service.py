from fastapi import HTTPException
import json
import httpx
from src.utilities.posts_parser import PostsParser
from .constants import GET_PUBLIC_TIMELINE_URL, GET_TAG_URL

class TimelineService():
    def __init__(self):
        self.parser = PostsParser()

    async def fetch_timeline(self):
        try:
            response = httpx.get(GET_PUBLIC_TIMELINE_URL)
        except Exception:
            raise HTTPException(
                status_code=500, detail="Error retrieving data from service")

        response_object = json.loads(response.content)
        data = self.parser.parse(response_object)
        return data

    async def fetch_timeline_by_tag(self, tag: str):
        try:
            response = httpx.get(GET_TAG_URL + tag + "?limit=30")
        except Exception:
            raise HTTPException(
                status_code=500, detail="Error retrieving data from service")

        response_object = json.loads(response.content)
        data = self.parser.parse(response_object)
        return data
