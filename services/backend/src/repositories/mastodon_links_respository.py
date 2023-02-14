from fastapi import HTTPException
import json
import httpx
from src.utilities import MastodonLinksParser
from ..repositories.constants import GET_TRENDING_LINKS_URL

class MastodonLinksRepository():

    def __init__(self):
        self.parser = MastodonLinksParser()

    async def fetch_trending_links(self):
        try:
            response = httpx.get(GET_TRENDING_LINKS_URL)
        except Exception:
            raise HTTPException(
                status_code=500, detail="Error retrieving data from service")

        response_object = json.loads(response.content)
        data = self.parser.parse(response_object)

        return data

