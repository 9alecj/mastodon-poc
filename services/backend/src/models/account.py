from datetime import datetime
from typing import List, Any

class Account:
    id: str
    username: str
    acct: str
    display_name: str
    locked: bool
    bot: bool
    discoverable: bool
    group: bool
    created_at: datetime
    note: str
    url: str
    avatar: str
    avatar_static: str
    header: str
    header_static: str
    followers_count: int
    following_count: int
    statuses_count: int
    last_status_at: datetime
    emojis: List[Any]
    fields: List[Any]

    def __init__(self, id: str, username: str, acct: str, display_name: str, locked: bool, bot: bool, discoverable: bool, group: bool, created_at: datetime, note: str, url: str, avatar: str, avatar_static: str, header: str, header_static: str, followers_count: int, following_count: int, statuses_count: int, last_status_at: datetime, emojis: List[Any], fields: List[Any]) -> None:
        self.id = id
        self.username = username
        self.acct = acct
        self.display_name = display_name
        self.locked = locked
        self.bot = bot
        self.discoverable = discoverable
        self.group = group
        self.created_at = created_at
        self.note = note
        self.url = url
        self.avatar = avatar
        self.avatar_static = avatar_static
        self.header = header
        self.header_static = header_static
        self.followers_count = followers_count
        self.following_count = following_count
        self.statuses_count = statuses_count
        self.last_status_at = last_status_at
        self.emojis = emojis
        self.fields = fields