from fastapi import HTTPException
import json
import httpx
from src.utilities import LinksParser, PostsParser, TrendsParser
from .constants import GET_TRENDING_STATUSES_URL, GET_TRENDING_LINKS_URL, GET_TRENDS_URL

class TrendsService():

    def __init__(self):
        self.trends_parser = TrendsParser()
        self.links_parser = LinksParser()
        self.post_parser = PostsParser()

    async def fetch_trending_statuses(self):
        try:
            response = httpx.get(GET_TRENDING_STATUSES_URL)
        except Exception:
            raise HTTPException(
                status_code=500, detail="Error retrieving data from service")

        response_object = json.loads(response.content)
        data = self.post_parser.parse(response_object)
        return data


    async def fetch_trending_links(self):
        try:
            response = httpx.get(GET_TRENDING_LINKS_URL)
        except Exception:
            raise HTTPException(
                status_code=500, detail="Error retrieving data from service")

        response_object = json.loads(response.content)
        data = self.links_parser.parse(response_object)

        return data


    async def fetch_trends(self):
        try:
            response = httpx.get(GET_TRENDS_URL)
        except Exception:
            raise HTTPException(
                status_code=500, detail="Error retrieving data from service")

        response_object = json.loads(response.content)
        data = self.trends_parser.parse(response_object)

        return data
