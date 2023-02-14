from src.repositories import MastodonTagsRepository

class TagsService():

    def __init__(self):
        self.tags_repo = MastodonTagsRepository()

    async def get_trending_tags(self):
        return await self.tags_repo.fetch_trending_tags()
