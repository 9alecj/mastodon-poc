import json
import requests




def get_sample_trending_links_data():
    response = requests.get("https://mastodon.social/api/v1/trends/links")
    response_object = json.loads(response.content)

    trending_links_filename = "trending_links_sample_file.json"

    trending_links_sample_file = open(trending_links_filename, "w")
    with open(trending_links_filename, 'w') as f:
        json.dump(response_object, f)

    trending_links_sample_file.close()



def get_sample_trending_statuses_data():
    response = requests.get("https://mastodon.social/api/v1/trends/statuses")
    response_object = json.loads(response.content)

    trending_statuses_filename = "trending_statuses_sample_file.json"

    trending_statuses_sample_file = open(trending_statuses_filename, "w")
    with open(trending_statuses_filename, 'w') as f:
        json.dump(response_object, f)

    trending_statuses_sample_file.close()



def get_sample_timeline_data():
    response = requests.get("https://mastodon.social/api/v1/timelines/public?limit=10")
    response_object = json.loads(response.content)

    timeline_filename = "timeline_sample_file.json"

    timeline_sample_file = open(timeline_filename, "w")
    with open(timeline_filename, 'w') as f:
        json.dump(response_object, f)

    timeline_sample_file.close()

def get_sample_trends_data():
    response = requests.get("https://mastodon.social/api/v1/trends")
    response_object = json.loads(response.content)

    trends_filename = "trends_sample_file.json"

    trends_sample_file = open(trends_filename, "w")
    with open(trends_filename, 'w') as f:
        json.dump(response_object, f)

    trends_sample_file.close()

def get_sample_tags_data():
    response = requests.get("https://mastodon.social/api/v1/timelines/tag/" + "cats")
    response_object = json.loads(response.content)

    tags_filename = "tags_sample_file.json"

    tags_sample_file = open(tags_filename, "w")
    with open(tags_filename, 'w') as f:
        json.dump(response_object, f)

    tags_sample_file.close()



def main():
    get_sample_trends_data()
    get_sample_trending_statuses_data()
    get_sample_trending_links_data()
    get_sample_timeline_data()
    get_sample_tags_data()

if __name__ == "__main__":
    main()