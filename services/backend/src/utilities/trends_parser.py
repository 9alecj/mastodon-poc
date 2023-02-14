from fastapi import HTTPException
from src.utilities.parse_interface import ParserInterface
from src.viewmodels import TrendViewModel

class TrendsParser():
    def parse(self, trends):
        data = []
        try:
            for trend in trends:
                item = TrendViewModel(
                    name=trend["name"],
                )
                data.append(item)
            return data
        except Exception:
            raise HTTPException(
                status_code=500, detail="Error parsing data from service")
