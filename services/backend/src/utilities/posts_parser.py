from fastapi import HTTPException

def parse_posts(posts):
    data = []
    try:
        for post in posts:
            item = Post( 
                    profile_photo = post["account"]["avatar"],
                    id = post["id"],
                    username = post["account"]["username"],
                    content = post["content"],
                    media = post["media_attachments"][0]["url"] if post["media_attachments"] else None,
                    post_time = post["created_at"],
                    replies_count = post["replies_count"],
                    reblogs_count = post["reblogs_count"],
                    favourites_count = post["favourites_count"]
                )
            data.append(item)
        return data
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=e)


class Post:
    def __init__ (self, profile_photo, id, username, 
    content, media, post_time, replies_count, reblogs_count, favourites_count):
        self.profile_photo = profile_photo
        self.id = id
        self.username = username
        self.content = content
        self.media = media
        self.post_time = post_time
        self.replies_count = replies_count
        self.reblogs_count = reblogs_count
        self.favourites_count = favourites_count