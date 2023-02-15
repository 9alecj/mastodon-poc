from fastapi import HTTPException
from src.viewmodels import PostViewModel
from bs4 import BeautifulSoup



class MicroblogPostsParser():
    def parse(self, posts):
        data = []

        try:
            for post in posts["items"]:
                soup = BeautifulSoup(post["content_html"], 'html.parser')
                media = None
                if soup.img:
                    media = str(soup.img['src'])
                    print("image: " + media)
                    soup.img.decompose()

                content = str(soup)
                print("content: " + content)
                
                item = PostViewModel(
                    profile_photo=post["author"]["avatar"],
                    id=post["id"],
                    username=post["author"]["_microblog"]["username"],
                    name=post["author"]["name"],
                    content=content,
                    media= media,
                    post_time=post["date_published"],
                    replies_count=None,
                    reblogs_count=None,
                    favourites_count=None,
                    application="micro.blog",
                    url=post["url"]
                )
                data.append(item)
            return data
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=500, detail="error parsing data from service: " + str(e))
