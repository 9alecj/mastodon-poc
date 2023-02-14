from src.repositories import MastodonLinksRepository

class LinksService():

    def __init__(self):
        self.links_repository = MastodonLinksRepository()

    async def get_trending_links(self):
        return await self.links_repository.fetch_trending_links()

