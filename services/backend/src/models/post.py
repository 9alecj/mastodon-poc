from datetime import datetime
from typing import List, Any, Optional
from .account import Account
from .tag import Tag
from .application import Application
from dataclasses import dataclass


@dataclass
class Post:
    id: str
    created_at: datetime
    account: Account
    tags: List[Tag]
    media_attachments: List[Any]
    mentions: List[Any]
    emojis: List[Any]
    in_reply_to_id: None
    in_reply_to_account_id: None
    sensitive: bool
    spoiler_text: str
    visibility: str
    language: str
    uri: str
    url: str
    replies_count: int
    reblogs_count: int
    favourites_count: int
    edited_at: None
    content: str
    reblog: None
    application: Application
    card: None
    poll: None
