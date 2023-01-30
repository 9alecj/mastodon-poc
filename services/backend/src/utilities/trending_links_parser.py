from http.client import HTTPException

def parse_links(links):
    data = []
    try:
        for link in links:
            item = Link( 
                    url = link["url"],
                    title = link["title"],
                    description = link["description"],
                    author_name = link["author_name"],
                    provider_name = link["provider_name"],
                    image = link["image"],
                    blurhash = link["blurhash"]
                )
            data.append(item)
        return data
    except Exception:
        raise HTTPException(status_code=500, detail="Error parsing data from service")
class Link:
    def __init__ (self, url, title, description, 
    author_name, provider_name, image, blurhash):
        self.url = url
        self.title = title
        self.description = description
        self.author_name = author_name
        self.provider_name = provider_name
        self.image = image
        self.blurhash = blurhash