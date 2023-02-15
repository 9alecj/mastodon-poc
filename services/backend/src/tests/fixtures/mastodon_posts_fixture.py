import pytest
from src.viewmodels import PostViewModel


def expected_posts_success():
    sample_post_data = []
    sample_post_data.append(PostViewModel(
        profile_photo="https://files.mastodon.social/accounts/avatars/001/021/813/original/feeb19e419f0e3c4.jpg",
        id="109761844504564708",
        username="Some_Emo_Chick",
        name="Frankie \u2705",
        content="<p>The Onion never misses</p>",
        media="https://files.mastodon.social/media_attachments/files/109/761/841/472/834/189/original/b79eebc4402ae01b.png",
        post_time="2023-01-27T15:20:32.415Z",
        replies_count=12,
        reblogs_count=753,
        favourites_count=1111,
        application="mastodon"))
    sample_post_data.append(PostViewModel(
                            profile_photo="https://files.mastodon.social/accounts/avatars/000/276/336/original/a2fc430ff065be26.jpg",
                            id="109762190140654574",
                            username="lizzard",
                            name="lizzard",
                            content="<p>Happy Large Boulder the Size of a Small Boulder Day! Please celebrate by posting pictures of rocks of indeterminate sizes or maybe your favorite boulder</p>",
                            media="https://files.mastodon.social/media_attachments/files/109/762/181/711/458/430/original/e0a3dec6cba76e3a.png",
                            post_time="2023-01-27T16:48:26.402Z",
                            replies_count=37,
                            reblogs_count=320,
                            favourites_count=432,
                            application="mastodon"))
    return sample_post_data


def sample_posts_json_success():
    return [
        {
            "id": "109761844504564708",
            "created_at": "2023-01-27T15:20:32.415Z",
            "in_reply_to_id": None,
            "in_reply_to_account_id": None,
            "sensitive": False,
            "spoiler_text": "",
            "visibility": "public",
            "language": "en",
            "uri": "https://mastodon.social/users/Some_Emo_Chick/statuses/109761844504564708",
            "url": "https://mastodon.social/@Some_Emo_Chick/109761844504564708",
            "replies_count": 12,
            "reblogs_count": 753,
            "favourites_count": 1111,
            "edited_at": None,
            "content": "<p>The Onion never misses</p>",
            "reblog": None,
            "application": {
                "name": "Web",
                "website": None
            },
            "account": {
                "id": "1021813",
                "username": "Some_Emo_Chick",
                "acct": "Some_Emo_Chick",
                "display_name": "Frankie \u2705",
                "locked": False,
                "bot": False,
                "discoverable": True,
                "group": False,
                "created_at": "2019-12-05T00:00:00.000Z",
                "note": "<p>Michigan girl talking about: Politics, Religion, Art, Beauty, Equality, Star Trek, STO, Pansexuality, and Things I Should Probably Not Be Saying Out Loud.</p>",
                "url": "https://mastodon.social/@Some_Emo_Chick",
                "avatar": "https://files.mastodon.social/accounts/avatars/001/021/813/original/feeb19e419f0e3c4.jpg",
                "avatar_static": "https://files.mastodon.social/accounts/avatars/001/021/813/original/feeb19e419f0e3c4.jpg",
                "header": "https://files.mastodon.social/accounts/headers/001/021/813/original/873922c4bae33b55.png",
                "header_static": "https://files.mastodon.social/accounts/headers/001/021/813/original/873922c4bae33b55.png",
                "followers_count": 7913,
                "following_count": 154,
                "statuses_count": 9056,
                "last_status_at": "2023-01-27",
                "noindex": False,
                "emojis": [],
                "fields": [
                        {
                            "name": "Reddit",
                            "value": "<a href=\"https://www.reddit.com/user/FAMDetroit\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://www.</span><span class=\"\">reddit.com/user/FAMDetroit</span><span class=\"invisible\"></span></a>",
                            "verified_at": None
                        },
                    {
                            "name": "Tumblr",
                            "value": "<a href=\"https://someemochick.tumblr.com/\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">someemochick.tumblr.com/</span><span class=\"invisible\"></span></a>",
                            "verified_at": "2022-08-10T20:58:25.835+00:00"
                    }
                ]
            },
            "media_attachments": [
                {
                    "id": "109761841472834189",
                    "type": "image",
                    "url": "https://files.mastodon.social/media_attachments/files/109/761/841/472/834/189/original/b79eebc4402ae01b.png",
                    "preview_url": "https://files.mastodon.social/media_attachments/files/109/761/841/472/834/189/small/b79eebc4402ae01b.png",
                    "remote_url": None,
                    "preview_remote_url": None,
                    "text_url": None,
                    "meta": {
                            "original": {
                                "width": 960,
                                "height": 782,
                                "size": "960x782",
                                "aspect": 1.227621483375959
                            },
                        "small": {
                                "width": 532,
                                "height": 433,
                                "size": "532x433",
                                "aspect": 1.2286374133949192
                                },
                        "focus": {
                                "x": 0.0,
                                "y": 0.0
                                }
                    },
                    "description": "Satire headline: Police urge calm in light of unspeakable evil they did",
                    "blurhash": "UARypZ9F~qofNZxu%Mj[.8%M%May9FWB?IWB"
                }
            ],
            "mentions": [],
            "tags": [],
            "emojis": [],
            "card": None,
            "poll": None
        },
        {
            "id": "109762190140654574",
            "created_at": "2023-01-27T16:48:26.402Z",
            "in_reply_to_id": None,
            "in_reply_to_account_id": None,
            "sensitive": False,
            "spoiler_text": "",
            "visibility": "public",
            "language": "en",
            "uri": "https://mastodon.social/users/lizzard/statuses/109762190140654574",
            "url": "https://mastodon.social/@lizzard/109762190140654574",
            "replies_count": 37,
            "reblogs_count": 320,
            "favourites_count": 432,
            "edited_at": None,
            "content": "<p>Happy Large Boulder the Size of a Small Boulder Day! Please celebrate by posting pictures of rocks of indeterminate sizes or maybe your favorite boulder</p>",
            "reblog": None,
            "application": {
                "name": "Web",
                "website": None
            },
            "account": {
                "id": "276336",
                "username": "lizzard",
                "acct": "lizzard",
                "display_name": "lizzard",
                "locked": False,
                "bot": False,
                "discoverable": True,
                "group": False,
                "created_at": "2018-01-20T00:00:00.000Z",
                "note": "<p>overanalyzes everything and really, really, wonders why. they/them. <span class=\"h-card\"><a href=\"https://mastodon.social/@lizzard\" class=\"u-url mention\">@<span>lizzard</span></a></span></p><p>Liz Henry - writer, translator, blogger, book lover, hackerspace enthusiast, queer/trans disability justice activist, wheelchair user. San Francisco.  <a href=\"https://mastodon.social/tags/DisabilityJustice\" class=\"mention hashtag\" rel=\"tag\">#<span>DisabilityJustice</span></a></p>",
                "url": "https://mastodon.social/@lizzard",
                "avatar": "https://files.mastodon.social/accounts/avatars/000/276/336/original/a2fc430ff065be26.jpg",
                "avatar_static": "https://files.mastodon.social/accounts/avatars/000/276/336/original/a2fc430ff065be26.jpg",
                "header": "https://files.mastodon.social/accounts/headers/000/276/336/original/bd6e94c2f65766df.jpg",
                "header_static": "https://files.mastodon.social/accounts/headers/000/276/336/original/bd6e94c2f65766df.jpg",
                "followers_count": 1111,
                "following_count": 519,
                "statuses_count": 1157,
                "last_status_at": "2023-01-27",
                "noindex": False,
                "emojis": [],
                "fields": [
                        {
                            "name": "blog",
                            "value": "<a href=\"https://bookmaniac.org\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">bookmaniac.org</span><span class=\"invisible\"></span></a>",
                            "verified_at": None
                        },
                    {
                            "name": "books",
                            "value": "<a href=\"https://www.amazon.com/kindle-dbs/entity/author/B007Z8R8NM\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://www.</span><span class=\"ellipsis\">amazon.com/kindle-dbs/entity/a</span><span class=\"invisible\">uthor/B007Z8R8NM</span></a>",
                            "verified_at": None
                    },
                    {
                            "name": "games",
                            "value": "<a href=\"https://drlizzardo.itch.io/\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">drlizzardo.itch.io/</span><span class=\"invisible\"></span></a>",
                            "verified_at": None
                    },
                    {
                            "name": "poetry",
                            "value": "<a href=\"https://bookmaniac.org/poetry/\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">bookmaniac.org/poetry/</span><span class=\"invisible\"></span></a>",
                            "verified_at": None
                    }
                ]
            },
            "media_attachments": [
                {
                    "id": "109762181711458430",
                    "type": "image",
                    "url": "https://files.mastodon.social/media_attachments/files/109/762/181/711/458/430/original/e0a3dec6cba76e3a.png",
                    "preview_url": "https://files.mastodon.social/media_attachments/files/109/762/181/711/458/430/small/e0a3dec6cba76e3a.png",
                    "remote_url": None,
                    "preview_remote_url": None,
                    "text_url": None,
                    "meta": {
                            "original": {
                                "width": 982,
                                "height": 1346,
                                "size": "982x1346",
                                "aspect": 0.7295690936106983
                            },
                        "small": {
                                "width": 410,
                                "height": 562,
                                "size": "410x562",
                                "aspect": 0.7295373665480427
                                },
                        "focus": {
                                "x": 0.0,
                                "y": 0.0
                                }
                    },
                    "description": "screencap of a tweet from jan 27, 2020 by the san miguel sheriff with a photo of a rock in the middle of a snowy road. Text reads \"Large boulder the size of a small boulder is completely blocking east-bound lane Highway 145 mm78 at Silverpick Rd. Please use caution and watch for emergency vehicles in the area.",
                    "blurhash": "USN1Ab%MWARj~qRjofof?bIUayWBofRjWBof"
                }
            ],
            "mentions": [],
            "tags": [],
            "emojis": [],
            "card": None,
            "poll": None
        }]


def sample_posts_json_fail():
    return [
        {
            "created_at": "2023-01-27T15:20:32.415Z",
            "in_reply_to_id": None,
            "in_reply_to_account_id": None,
            "sensitive": False,
            "spoiler_text": "",
            "visibility": "public",
            "language": "en",
            "uri": "https://mastodon.social/users/Some_Emo_Chick/statuses/109761844504564708",
            "url": "https://mastodon.social/@Some_Emo_Chick/109761844504564708",
            "replies_count": 12,
            "reblogs_count": 753,
            "favourites_count": 1111,
            "edited_at": None,
            "content": "<p>The Onion never misses</p>",
            "reblog": None,
            "application": {
                "name": "Web",
                "website": None
            },
            "account": {
                "id": "1021813",
                "username": "Some_Emo_Chick",
                "acct": "Some_Emo_Chick",
                "display_name": "Frankie \u2705",
                "locked": False,
                "bot": False,
                "discoverable": True,
                "group": False,
                "created_at": "2019-12-05T00:00:00.000Z",
                "note": "<p>Michigan girl talking about: Politics, Religion, Art, Beauty, Equality, Star Trek, STO, Pansexuality, and Things I Should Probably Not Be Saying Out Loud.</p>",
                "url": "https://mastodon.social/@Some_Emo_Chick",
                "avatar": "https://files.mastodon.social/accounts/avatars/001/021/813/original/feeb19e419f0e3c4.jpg",
                "avatar_static": "https://files.mastodon.social/accounts/avatars/001/021/813/original/feeb19e419f0e3c4.jpg",
                "header": "https://files.mastodon.social/accounts/headers/001/021/813/original/873922c4bae33b55.png",
                "header_static": "https://files.mastodon.social/accounts/headers/001/021/813/original/873922c4bae33b55.png",
                "followers_count": 7913,
                "following_count": 154,
                "statuses_count": 9056,
                "last_status_at": "2023-01-27",
                "noindex": False,
                "emojis": [],
                "fields": [
                        {
                            "name": "Reddit",
                            "value": "<a href=\"https://www.reddit.com/user/FAMDetroit\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://www.</span><span class=\"\">reddit.com/user/FAMDetroit</span><span class=\"invisible\"></span></a>",
                            "verified_at": None
                        },
                    {
                            "name": "Tumblr",
                            "value": "<a href=\"https://someemochick.tumblr.com/\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">someemochick.tumblr.com/</span><span class=\"invisible\"></span></a>",
                            "verified_at": "2022-08-10T20:58:25.835+00:00"
                    }
                ]
            },
            "media_attachments": [
                {
                    "id": "109761841472834189",
                    "type": "image",
                    "url": "https://files.mastodon.social/media_attachments/files/109/761/841/472/834/189/original/b79eebc4402ae01b.png",
                    "preview_url": "https://files.mastodon.social/media_attachments/files/109/761/841/472/834/189/small/b79eebc4402ae01b.png",
                    "remote_url": None,
                    "preview_remote_url": None,
                    "text_url": None,
                    "meta": {
                            "original": {
                                "width": 960,
                                "height": 782,
                                "size": "960x782",
                                "aspect": 1.227621483375959
                            },
                        "small": {
                                "width": 532,
                                "height": 433,
                                "size": "532x433",
                                "aspect": 1.2286374133949192
                                },
                        "focus": {
                                "x": 0.0,
                                "y": 0.0
                                }
                    },
                    "description": "Satire headline: Police urge calm in light of unspeakable evil they did",
                    "blurhash": "UARypZ9F~qofNZxu%Mj[.8%M%May9FWB?IWB"
                }
            ],
            "mentions": [],
            "tags": [],
            "emojis": [],
            "card": None,
            "poll": None
        },
        {
            "id": "109762190140654574",
            "created_at": "2023-01-27T16:48:26.402Z",
            "in_reply_to_id": None,
            "in_reply_to_account_id": None,
            "sensitive": False,
            "spoiler_text": "",
            "visibility": "public",
            "language": "en",
            "uri": "https://mastodon.social/users/lizzard/statuses/109762190140654574",
            "url": "https://mastodon.social/@lizzard/109762190140654574",
            "replies_count": 37,
            "reblogs_count": 320,
            "favourites_count": 432,
            "edited_at": None,
            "content": "<p>Happy Large Boulder the Size of a Small Boulder Day! Please celebrate by posting pictures of rocks of indeterminate sizes or maybe your favorite boulder</p>",
            "reblog": None,
            "application": {
                "name": "Web",
                "website": None
            },
            "account": {
                "id": "276336",
                "username": "lizzard",
                "acct": "lizzard",
                "display_name": "lizzard",
                "locked": False,
                "bot": False,
                "discoverable": True,
                "group": False,
                "created_at": "2018-01-20T00:00:00.000Z",
                "note": "<p>overanalyzes everything and really, really, wonders why. they/them. <span class=\"h-card\"><a href=\"https://mastodon.social/@lizzard\" class=\"u-url mention\">@<span>lizzard</span></a></span></p><p>Liz Henry - writer, translator, blogger, book lover, hackerspace enthusiast, queer/trans disability justice activist, wheelchair user. San Francisco.  <a href=\"https://mastodon.social/tags/DisabilityJustice\" class=\"mention hashtag\" rel=\"tag\">#<span>DisabilityJustice</span></a></p>",
                "url": "https://mastodon.social/@lizzard",
                "avatar": "https://files.mastodon.social/accounts/avatars/000/276/336/original/a2fc430ff065be26.jpg",
                "avatar_static": "https://files.mastodon.social/accounts/avatars/000/276/336/original/a2fc430ff065be26.jpg",
                "header": "https://files.mastodon.social/accounts/headers/000/276/336/original/bd6e94c2f65766df.jpg",
                "header_static": "https://files.mastodon.social/accounts/headers/000/276/336/original/bd6e94c2f65766df.jpg",
                "followers_count": 1111,
                "following_count": 519,
                "statuses_count": 1157,
                "last_status_at": "2023-01-27",
                "noindex": False,
                "emojis": [],
                "fields": [
                        {
                            "name": "blog",
                            "value": "<a href=\"https://bookmaniac.org\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">bookmaniac.org</span><span class=\"invisible\"></span></a>",
                            "verified_at": None
                        },
                    {
                            "name": "books",
                            "value": "<a href=\"https://www.amazon.com/kindle-dbs/entity/author/B007Z8R8NM\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://www.</span><span class=\"ellipsis\">amazon.com/kindle-dbs/entity/a</span><span class=\"invisible\">uthor/B007Z8R8NM</span></a>",
                            "verified_at": None
                    },
                    {
                            "name": "games",
                            "value": "<a href=\"https://drlizzardo.itch.io/\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">drlizzardo.itch.io/</span><span class=\"invisible\"></span></a>",
                            "verified_at": None
                    },
                    {
                            "name": "poetry",
                            "value": "<a href=\"https://bookmaniac.org/poetry/\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">bookmaniac.org/poetry/</span><span class=\"invisible\"></span></a>",
                            "verified_at": None
                    }
                ]
            },
            "media_attachments": [
                {
                    "id": "109762181711458430",
                    "type": "image",
                    "url": "https://files.mastodon.social/media_attachments/files/109/762/181/711/458/430/original/e0a3dec6cba76e3a.png",
                    "preview_url": "https://files.mastodon.social/media_attachments/files/109/762/181/711/458/430/small/e0a3dec6cba76e3a.png",
                    "remote_url": None,
                    "preview_remote_url": None,
                    "text_url": None,
                    "meta": {
                            "original": {
                                "width": 982,
                                "height": 1346,
                                "size": "982x1346",
                                "aspect": 0.7295690936106983
                            },
                        "small": {
                                "width": 410,
                                "height": 562,
                                "size": "410x562",
                                "aspect": 0.7295373665480427
                                },
                        "focus": {
                                "x": 0.0,
                                "y": 0.0
                                }
                    },
                    "description": "screencap of a tweet from jan 27, 2020 by the san miguel sheriff with a photo of a rock in the middle of a snowy road. Text reads \"Large boulder the size of a small boulder is completely blocking east-bound lane Highway 145 mm78 at Silverpick Rd. Please use caution and watch for emergency vehicles in the area.",
                    "blurhash": "USN1Ab%MWARj~qRjofof?bIUayWBofRjWBof"
                }
            ],
            "mentions": [],
            "tags": [],
            "emojis": [],
            "card": None,
            "poll": None
        }]
