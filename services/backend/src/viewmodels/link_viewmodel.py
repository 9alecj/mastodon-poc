class LinkViewModel:
    def __init__(self, url, title, description,
                 author_name, provider_name, image, blurhash):
        self.url = url
        self.title = title
        self.description = description
        self.author_name = author_name
        self.provider_name = provider_name
        self.image = image
        self.blurhash = blurhash