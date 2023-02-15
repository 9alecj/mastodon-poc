from src.repositories import MastodonPostsRepository, MicroBlogPostsRepository

class PostsService():
    def __init__(self):
        self.post_repo = MastodonPostsRepository()
        self.microblog_repo = MicroBlogPostsRepository()

    async def get_public_posts(self):
        mastodon_posts = await self.post_repo.fetch_public_posts()
        microblog_posts = await self.microblog_repo.fetch_public_posts()

        posts = zipPostLists(mastodon_posts, microblog_posts)

        return posts

    async def get_posts_by_tag(self, tag: str):
        return await self.post_repo.fetch_posts_by_tag(tag)

    async def get_trending_posts(self):
        mastodon_posts = await self.post_repo.fetch_trending_posts()
        microblog_posts = await self.microblog_repo.fetch_public_posts()

        posts = zipPostLists(mastodon_posts, microblog_posts)

        return posts


def zipPostLists(list1, list2):
    postTuples = zip(list1, list2)
    posts = []
    for postTuple in postTuples:
        for post in postTuple:
            posts.append(post)
    return posts
