def parse_trends(trends):
    data = []
    for trend in trends:
        item = Trend( 
                name = trend["name"],
            )
        data.append(item)
    return data

class Trend(object):
    def __init__ (self, name):
        self.name = name