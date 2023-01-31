from fastapi import HTTPException
import json
from typing import Optional
import httpx
from .constants import GET_PUBLIC_TIMELINE_URL, GET_TAG_URL

from ..utilities.posts_parser import parse_posts


async def fetch_timeline():
    try:
        response = httpx.get(GET_PUBLIC_TIMELINE_URL)
    except Exception:
        raise HTTPException(status_code=500, detail="Error retrieving data from service")
    
    response_object = json.loads(response.content)
    data = parse_posts(response_object)
    return data

async def fetch_timeline_by_tag(tag: str):
    try:
        response = httpx.get(GET_TAG_URL + tag)
    except Exception:
        raise HTTPException(status_code=500, detail="Error retrieving data from service")
    
    response_object = json.loads(response.content)
    data = parse_posts(response_object)
    return data
