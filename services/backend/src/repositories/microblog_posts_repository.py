from fastapi import HTTPException
import json
import httpx
from src.utilities import MicroblogPostsParser
from .constants import GET_PUBLIC_TIMELINE_URL

class MicroBlogPostsRepository():
    def __init__(self):
        self.parser = MicroblogPostsParser()

    async def fetch_public_posts(self):
        try:
            response = httpx.get("https://micro.blog/posts/discover")
        except Exception:
            raise HTTPException(
                status_code=500, detail="Error retrieving data from service")

        response_object = json.loads(response.content)
        data = self.parser.parse(response_object)
        return data[:30]