

class PostViewModel:
    def __init__(self, profile_photo, id, username, name, content, media, post_time,
                    replies_count, reblogs_count, favourites_count, application, url):
        self.profile_photo = profile_photo
        self.id = id
        self.username = username
        self.name = name
        self.content = content 
        self.media = media
        self.post_time = post_time
        self.replies_count = replies_count
        self.reblogs_count = reblogs_count
        self.favourites_count = favourites_count
        self.application=application
        self.url = url
