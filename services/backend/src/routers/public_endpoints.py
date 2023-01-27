import json
from typing import Optional
from fastapi import APIRouter 
from .post_parser import parse_posts
from .trending_link_parser import parse_links
from .trends_parser import parse_trends

import httpx

router = APIRouter()
get_public_timeline_url = "https://mastodon.social/api/v1/timelines/public?limit=20"
get_trending_links_url = "https://mastodon.social/api/v1/trends/links?limit=20"
get_trending_statuses_url = "https://mastodon.social/api/v1/trends/statuses?limit=20"
get_trends_url = "https://mastodon.social/api/v1/trends"
get_tag_url = "https://mastodon.social/api/v1/timelines/tag/"



@router.get("/public", tags=["public"])
async def get_public_timeline(tag: Optional[str] = None):

    print("tag: " + tag)
    url = ""
    if tag:
        url = get_tag_url + tag
    else:
        url = get_public_timeline_url

    try:
        response = httpx.get(url)
        response_object = json.loads(response.content)
        data = parse_posts(response_object)
        return data
    except Exception as e:
        print(e)
        return e
    

@router.get("/trending-statuses", tags=["public"])
async def get_trending_statuses():
    
    try:
        response = httpx.get(get_trending_statuses_url)
        response_object = json.loads(response.content)
        data = parse_posts(response_object)
        return data
    except Exception as e:
        print(e)
        return e

@router.get("/trending-links", tags=["public"])
async def get_trending_links():
    response = httpx.get(get_trending_links_url)
    response_object = json.loads(response.content)
    data = parse_links(response_object)

    return data

@router.get("/trends", tags=["public"])
async def get_trends():
    response = httpx.get(get_trends_url)
    response_object = json.loads(response.content)
    data = parse_trends(response_object)

    return data