from fastapi import HTTPException
import json
import httpx
from ..utilities.links_parser import parse_links
from ..utilities.posts_parser import parse_posts
from ..utilities.trends_parser import parse_trends
from .constants import GET_TRENDING_STATUSES_URL, GET_TRENDING_LINKS_URL, GET_TRENDS_URL

async def fetch_trending_statuses():
    try:
        response = httpx.get(GET_TRENDING_STATUSES_URL)
    except Exception:
        raise HTTPException(status_code=500, detail="Error retrieving data from service")

    response_object = json.loads(response.content)
    data = parse_posts(response_object)
    return data
    

async def fetch_trending_links():
    try:
        response = httpx.get(GET_TRENDING_LINKS_URL)
    except Exception:
        raise HTTPException(status_code=500, detail="Error retrieving data from service")
    
    response_object = json.loads(response.content)
    data = parse_links(response_object)

    return data

async def fetch_trends():
    try:
        response = httpx.get(GET_TRENDS_URL)
    except Exception:
        raise HTTPException(status_code=500, detail="Error retrieving data from service")
    
    response_object = json.loads(response.content)
    data = parse_trends(response_object)

    return data