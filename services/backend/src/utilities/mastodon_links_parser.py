from fastapi import HTTPException
from src.viewmodels import LinkViewModel

class MastodonLinksParser():
    def parse(self, links):
        data = []
        try:
            for link in links:
                item = LinkViewModel(
                    url=link["url"],
                    title=link["title"],
                    description=link["description"],
                    author_name=link["author_name"],
                    provider_name=link["provider_name"],
                    image=link["image"],
                    blurhash=link["blurhash"]
                )
                data.append(item)
            return data
        except Exception:
            raise HTTPException(
                status_code=500, detail="Error parsing data from service")
