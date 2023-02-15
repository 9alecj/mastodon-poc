from src.viewmodels.post_viewmodel import PostViewModel


def expected_posts_success():
    sample_post_data = []
    sample_post_data.append(PostViewModel(
        profile_photo="https://micro.blog/mbkriegh/avatar.jpg",
        id="16997087",
        username="mbkriegh",
        name="Michael Bogdanffy-kriegh",
        content="<p>Inspired by a fellow Micro.blogger, I don’t remember who it was, I made a Dutch Baby for our Valentines Day breakfast…</p>\n\n",
        media="https://cdn.micro.blog/photos/1000x/https%3A%2F%2Fcdn.uploads.micro.blog%2F38689%2F2023%2F5b996ddd7a.jpg",
        post_time="2023-02-14T15:12:44+00:00",
        replies_count=None,
        reblogs_count=None,
        favourites_count=None,
        application="micro.blog",
        url="https://www.notesonattentionpaid.com/2023/02/14/inspired-by-a.html"))
    sample_post_data.append(PostViewModel(
                            profile_photo="https://avatars.micro.blog/avatars/2023/02/131.jpg",
                            id="16997071",
                            username="jack",
                            name="Jack Baty",
                            content="<p>My only real issue with the Pilot Custom 823 fountain pen is that holds so much ink that I get bored using the same color for so long. Otherwise, it's perfect.</p>",
                            media=None,
                            post_time="2023-02-14T15:11:20+00:00",
                            replies_count=None,
                            reblogs_count=None,
                            favourites_count=None,
                            application="micro.blog",
                            url="https://baty.social/@jack/109863729915144541"))
    return sample_post_data



def sample_posts_json_success():
    return {
    "version": "https://jsonfeed.org/version/1",
    "title": "Micro.blog - Discover",
    "home_page_url": "https://micro.blog/",
    "feed_url": "https://micro.blog/posts/discover",
    "_microblog": {
      "about": "https://micro.blog/about/api",
      "tagmoji": [
        {
          "name": "photos",
          "title": "photos",
          "emoji": "📷",
          "is_featured": True
        },
        {
          "name": "books",
          "title": "books",
          "emoji": "📚",
          "is_featured": True
        },
        {
          "name": "tv",
          "title": "tv",
          "emoji": "📺",
          "is_featured": True
        },
        {
          "name": "music",
          "title": "music",
          "emoji": "🎵",
          "is_featured": True
        },
        {
          "name": "podcasts",
          "title": "podcasts",
          "emoji": "🎙️",
          "is_featured": True
        },
        {
          "name": "soccer",
          "title": "soccer",
          "emoji": "⚽️",
          "is_featured": True
        },
        {
          "name": "movies",
          "title": "movies",
          "emoji": "🍿",
          "is_featured": True
        },
        {
          "name": "knitting",
          "title": "knitting & crochet",
          "emoji": "🧶",
          "is_featured": True
        },
        {
          "name": "bread",
          "title": "bread",
          "emoji": "🍞",
          "is_featured": True
        },
        {
          "name": "writing",
          "title": "writing",
          "emoji": "📝",
          "is_featured": True
        },
        {
          "name": "gardening",
          "title": "gardening",
          "emoji": "🌱",
          "is_featured": True
        },
        {
          "name": "quotes",
          "title": "quotes",
          "emoji": "💬",
          "is_featured": True
        },
        {
          "name": "pens",
          "title": "pens & ink",
          "emoji": "🖋️",
          "is_featured": True
        },
        {
          "name": "football",
          "title": "football",
          "emoji": "🏈",
          "is_featured": False
        },
        {
          "name": "startrek",
          "title": "Star Trek",
          "emoji": "🖖",
          "is_featured": False
        },
        {
          "name": "rocket",
          "title": "rocket",
          "emoji": "🚀",
          "is_featured": False
        },
        {
          "name": "videogames",
          "title": "video games",
          "emoji": "🎮",
          "is_featured": False
        },
        {
          "name": "micromonday",
          "title": "Micro Monday",
          "emoji": "📅",
          "is_featured": False
        },
        {
          "name": "basketball",
          "title": "basketball",
          "emoji": "🏀",
          "is_featured": False
        },
        {
          "name": "baseball",
          "title": "baseball",
          "emoji": "⚾️",
          "is_featured": False
        },
        {
          "name": "travel",
          "title": "travel",
          "emoji": "🗺",
          "is_featured": False
        },
        {
          "name": "cricket",
          "title": "cricket",
          "emoji": "🏏",
          "is_featured": False
        },
        {
          "name": "breakfast",
          "title": "breakfast",
          "emoji": "🥞",
          "is_featured": False
        },
        {
          "name": "racing",
          "title": "racing",
          "emoji": "🏎️",
          "is_featured": False
        },
        {
          "name": "guitar",
          "title": "guitar",
          "emoji": "🎸",
          "is_featured": False
        },
        {
          "name": "art",
          "title": "art",
          "emoji": "🎨",
          "is_featured": False
        },
        {
          "name": "camping",
          "title": "camping",
          "emoji": "🏕️",
          "is_featured": False
        },
        {
          "name": "beer",
          "title": "beer",
          "emoji": "🍺",
          "is_featured": False
        },
        {
          "name": "wine",
          "title": "wine",
          "emoji": "🍷",
          "is_featured": False
        },
        {
          "name": "cats",
          "title": "cats",
          "emoji": "🐈",
          "is_featured": False
        },
        {
          "name": "dogs",
          "title": "dogs",
          "emoji": "🐕",
          "is_featured": False
        },
        {
          "name": "lgbtq",
          "title": "LGBTQ+",
          "emoji": "🏳️‍🌈",
          "is_featured": False
        },
        {
          "name": "coffee",
          "title": "coffee",
          "emoji": "☕️",
          "is_featured": False
        },
        {
          "name": "running",
          "title": "running",
          "emoji": "🏃",
          "is_featured": False
        },
        {
          "name": "wwdc",
          "title": "WWDC",
          "emoji": "🤯",
          "is_featured": False
        },
        {
          "name": "cycling",
          "title": "cycling",
          "emoji": "🚲",
          "is_featured": False
        },
        {
          "name": "adayinthelife2",
          "title": "A Day in the Life 2022",
          "emoji": "📷",
          "is_featured": False
        }
      ]
    },
    "items": [
      {
        "id": "16997087",
        "content_html": "<p>Inspired by a fellow Micro.blogger, I don’t remember who it was, I made a Dutch Baby for our Valentines Day breakfast…</p>\n<img src=\"https://cdn.micro.blog/photos/1000x/https%3A%2F%2Fcdn.uploads.micro.blog%2F38689%2F2023%2F5b996ddd7a.jpg\" width=\"600\" height=\"600\" alt=\"\" loading=\"lazy\">\n",
        "url": "https://www.notesonattentionpaid.com/2023/02/14/inspired-by-a.html",
        "date_published": "2023-02-14T15:12:44+00:00",
        "author": {
          "name": "Michael Bogdanffy-kriegh",
          "url": "https://mbkriegh.micro.blog/",
          "avatar": "https://micro.blog/mbkriegh/avatar.jpg",
          "_microblog": {
            "username": "mbkriegh"
          }
        },
        "_microblog": {
          "date_relative": "3:12 pm",
          "date_timestamp": 1676387564,
          "is_favorite": False,
          "is_bookmark": False,
          "is_deletable": False,
          "is_conversation": True,
          "is_linkpost": False,
          "is_mention": False
        }
      },
      {
        "id": "16997071",
        "content_html": "<p>My only real issue with the Pilot Custom 823 fountain pen is that holds so much ink that I get bored using the same color for so long. Otherwise, it's perfect.</p>",
        "url": "https://baty.social/@jack/109863729915144541",
        "date_published": "2023-02-14T15:11:20+00:00",
        "author": {
          "name": "Jack Baty",
          "url": "https://baty.net/",
          "avatar": "https://avatars.micro.blog/avatars/2023/02/131.jpg",
          "_microblog": {
            "username": "jack"
          }
        },
        "_microblog": {
          "date_relative": "3:11 pm",
          "date_timestamp": 1676387480,
          "is_favorite": False,
          "is_bookmark": False,
          "is_deletable": False,
          "is_conversation": True,
          "is_linkpost": False,
          "is_mention": False
        }
      }
    ]
}

def sample_posts_json_fail():
    return {
    "version": "https://jsonfeed.org/version/1",
    "title": "Micro.blog - Discover",
    "home_page_url": "https://micro.blog/",
    "feed_url": "https://micro.blog/posts/discover",
    "_microblog": {
      "about": "https://micro.blog/about/api",
      "tagmoji": [
        {
          "name": "photos",
          "title": "photos",
          "emoji": "📷",
          "is_featured": True
        },
        {
          "name": "books",
          "title": "books",
          "emoji": "📚",
          "is_featured": True
        },
        {
          "name": "tv",
          "title": "tv",
          "emoji": "📺",
          "is_featured": True
        },
        {
          "name": "music",
          "title": "music",
          "emoji": "🎵",
          "is_featured": True
        },
        {
          "name": "podcasts",
          "title": "podcasts",
          "emoji": "🎙️",
          "is_featured": True
        },
        {
          "name": "soccer",
          "title": "soccer",
          "emoji": "⚽️",
          "is_featured": True
        },
        {
          "name": "movies",
          "title": "movies",
          "emoji": "🍿",
          "is_featured": True
        },
        {
          "name": "knitting",
          "title": "knitting & crochet",
          "emoji": "🧶",
          "is_featured": True
        },
        {
          "name": "bread",
          "title": "bread",
          "emoji": "🍞",
          "is_featured": True
        },
        {
          "name": "writing",
          "title": "writing",
          "emoji": "📝",
          "is_featured": True
        },
        {
          "name": "gardening",
          "title": "gardening",
          "emoji": "🌱",
          "is_featured": True
        },
        {
          "name": "quotes",
          "title": "quotes",
          "emoji": "💬",
          "is_featured": True
        },
        {
          "name": "pens",
          "title": "pens & ink",
          "emoji": "🖋️",
          "is_featured": True
        },
        {
          "name": "football",
          "title": "football",
          "emoji": "🏈",
          "is_featured": False
        },
        {
          "name": "startrek",
          "title": "Star Trek",
          "emoji": "🖖",
          "is_featured": False
        },
        {
          "name": "rocket",
          "title": "rocket",
          "emoji": "🚀",
          "is_featured": False
        },
        {
          "name": "videogames",
          "title": "video games",
          "emoji": "🎮",
          "is_featured": False
        },
        {
          "name": "micromonday",
          "title": "Micro Monday",
          "emoji": "📅",
          "is_featured": False
        },
        {
          "name": "basketball",
          "title": "basketball",
          "emoji": "🏀",
          "is_featured": False
        },
        {
          "name": "baseball",
          "title": "baseball",
          "emoji": "⚾️",
          "is_featured": False
        },
        {
          "name": "travel",
          "title": "travel",
          "emoji": "🗺",
          "is_featured": False
        },
        {
          "name": "cricket",
          "title": "cricket",
          "emoji": "🏏",
          "is_featured": False
        },
        {
          "name": "breakfast",
          "title": "breakfast",
          "emoji": "🥞",
          "is_featured": False
        },
        {
          "name": "racing",
          "title": "racing",
          "emoji": "🏎️",
          "is_featured": False
        },
        {
          "name": "guitar",
          "title": "guitar",
          "emoji": "🎸",
          "is_featured": False
        },
        {
          "name": "art",
          "title": "art",
          "emoji": "🎨",
          "is_featured": False
        },
        {
          "name": "camping",
          "title": "camping",
          "emoji": "🏕️",
          "is_featured": False
        },
        {
          "name": "beer",
          "title": "beer",
          "emoji": "🍺",
          "is_featured": False
        },
        {
          "name": "wine",
          "title": "wine",
          "emoji": "🍷",
          "is_featured": False
        },
        {
          "name": "cats",
          "title": "cats",
          "emoji": "🐈",
          "is_featured": False
        },
        {
          "name": "dogs",
          "title": "dogs",
          "emoji": "🐕",
          "is_featured": False
        },
        {
          "name": "lgbtq",
          "title": "LGBTQ+",
          "emoji": "🏳️‍🌈",
          "is_featured": False
        },
        {
          "name": "coffee",
          "title": "coffee",
          "emoji": "☕️",
          "is_featured": False
        },
        {
          "name": "running",
          "title": "running",
          "emoji": "🏃",
          "is_featured": False
        },
        {
          "name": "wwdc",
          "title": "WWDC",
          "emoji": "🤯",
          "is_featured": False
        },
        {
          "name": "cycling",
          "title": "cycling",
          "emoji": "🚲",
          "is_featured": False
        },
        {
          "name": "adayinthelife2",
          "title": "A Day in the Life 2022",
          "emoji": "📷",
          "is_featured": False
        }
      ]
    },
    "items": [
      {
        "id": "16997087",
        "content": "<p>Inspired by a fellow Micro.blogger, I don’t remember who it was, I made a Dutch Baby for our Valentines Day breakfast…</p>\n<img src=\"https://cdn.micro.blog/photos/1000x/https%3A%2F%2Fcdn.uploads.micro.blog%2F38689%2F2023%2F5b996ddd7a.jpg\" width=\"600\" height=\"600\" alt=\"\" loading=\"lazy\">\n",
        "url": "https://www.notesonattentionpaid.com/2023/02/14/inspired-by-a.html",
        "date_published": "2023-02-14T15:12:44+00:00",
        "author": {
          "name": "Michael Bogdanffy-kriegh",
          "url": "https://mbkriegh.micro.blog/",
          "avatar": "https://micro.blog/mbkriegh/avatar.jpg",
          "_microblog": {
            "username": "mbkriegh"
          }
        },
        "_microblog": {
          "date_relative": "3:12 pm",
          "date_timestamp": 1676387564,
          "is_favorite": False,
          "is_bookmark": False,
          "is_deletable": False,
          "is_conversation": True,
          "is_linkpost": False,
          "is_mention": False
        }
      },
      {
        "id": "16997071",
        "content": "<p>My only real issue with the Pilot Custom 823 fountain pen is that holds so much ink that I get bored using the same color for so long. Otherwise, it's perfect.</p>",
        "url": "https://baty.social/@jack/109863729915144541",
        "date_published": "2023-02-14T15:11:20+00:00",
        "author": {
          "name": "Jack Baty",
          "url": "https://baty.net/",
          "avatar": "https://avatars.micro.blog/avatars/2023/02/131.jpg",
          "_microblog": {
            "username": "jack"
          }
        },
        "_microblog": {
          "date_relative": "3:11 pm",
          "date_timestamp": 1676387480,
          "is_favorite": False,
          "is_bookmark": False,
          "is_deletable": False,
          "is_conversation": True,
          "is_linkpost": False,
          "is_mention": False
        }
      }
    ]
}
