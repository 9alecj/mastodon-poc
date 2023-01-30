from http.client import HTTPException


def parse_trends(trends):
    data = []
    try:
        for trend in trends:
            item = Trend( 
                    name = trend["name"],
                )
            data.append(item)
        return data
    except Exception:
        raise HTTPException(status_code=500, detail="Error parsing data from service")

class Trend:
    def __init__ (self, name):
        self.name = name