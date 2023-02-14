from src.repositories import MastodonPostsRepository

class PostsService():
    def __init__(self):
        self.post_repo = MastodonPostsRepository()

    async def get_public_posts(self):
        return await self.post_repo.fetch_public_posts()

    async def get_posts_by_tag(self, tag: str):
        return await self.post_repo.fetch_posts_by_tag(tag)

    async def get_trending_posts(self):
        return await self.post_repo.fetch_trending_posts()
