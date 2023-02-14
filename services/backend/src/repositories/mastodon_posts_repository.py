from fastapi import HTTPException
import json
import httpx
from src.utilities import MastodonPostsParser
from .constants import GET_PUBLIC_TIMELINE_URL, GET_TAG_URL, GET_TRENDING_STATUSES_URL

class MastodonPostsRepository():
    def __init__(self):
        self.parser = MastodonPostsParser()

    async def fetch_public_posts(self):
        try:
            response = httpx.get(GET_PUBLIC_TIMELINE_URL)
        except Exception:
            raise HTTPException(
                status_code=500, detail="Error retrieving data from service")

        response_object = json.loads(response.content)
        data = self.parser.parse(response_object)
        return data

    async def fetch_posts_by_tag(self, tag: str):
        try:
            response = httpx.get(GET_TAG_URL + tag + "?limit=30")
        except Exception:
            raise HTTPException(
                status_code=500, detail="Error retrieving data from service")

        response_object = json.loads(response.content)
        data = self.parser.parse(response_object)
        return data

    async def fetch_trending_posts(self):
        try:
            response = httpx.get(GET_TRENDING_STATUSES_URL)
        except Exception:
            raise HTTPException(
                status_code=500, detail="Error retrieving data from service")

        response_object = json.loads(response.content)
        data = self.parser.parse(response_object)
        return data
