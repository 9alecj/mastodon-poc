from fastapi import HTTPException
from src.viewmodels import PostViewModel

class MastodonPostsParser():
    def parse(self, posts):
        data = []

        try:
            for post in posts:
                item = PostViewModel(
                    profile_photo=post["account"]["avatar"],
                    id=post["id"],
                    username=post["account"]["username"],
                    name=post["account"]["display_name"],
                    content=post["content"],
                    media=post["media_attachments"][0]["url"] if post["media_attachments"] else None,
                    post_time=post["created_at"],
                    replies_count=post["replies_count"],
                    reblogs_count=post["reblogs_count"],
                    favourites_count=post["favourites_count"],
                    application="mastodon"
                )
                data.append(item)
            return data
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=500, detail="error parsing data from service")
