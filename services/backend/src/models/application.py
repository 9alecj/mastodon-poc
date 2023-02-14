class Application:
    name: str
    url: str

    def __init__(self, name: str, website: str) -> None:
        self.name = name
        self.website = website