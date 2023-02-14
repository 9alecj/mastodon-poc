from fastapi import HTTPException
import json
import httpx
from src.utilities import MastodonTagsParser
from ..repositories.constants import GET_TRENDS_URL

class MastodonTagsRepository():

    def __init__(self):
        self.parser = MastodonTagsParser()

    async def fetch_trending_tags(self):
        try:
            response = httpx.get(GET_TRENDS_URL)
        except Exception:
            raise HTTPException(
                status_code=500, detail="Error retrieving data from service")

        response_object = json.loads(response.content)
        data = self.parser.parse(response_object)

        return data

