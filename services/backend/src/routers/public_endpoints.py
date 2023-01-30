from typing import Optional
from fastapi import APIRouter

from ..services import timelines_service
from ..services import trends_service

router = APIRouter()

@router.get("/timelines", tags=["public"])
async def get_public_timeline(tag: Optional[str] = None):
    return await timelines_service.fetch_timeline()

@router.get("/timelines/tag", tags=["public"])
async def get_public_timeline(tag: Optional[str] = None):
    return await timelines_service.fetch_timeline_by_tag(tag)

@router.get("/trending-statuses", tags=["public"])
async def get_trending_statuses():
    return await trends_service.fetch_trending_statuses()

@router.get("/trending-links", tags=["public"])
async def get_trending_links():
    return await trends_service.fetch_trending_links()

@router.get("/trends", tags=["public"])
async def get_trends():
    return await trends_service.fetch_trends()