import json

from .fixtures.posts_fixture import sample_posts_json
from ..utilities.posts_parser import Post, parse_posts
import pytest

def test_read_main(sample_posts_json):
    sample_post_data = []
    sample_post_data.append(Post(
                                profile_photo="https://files.mastodon.social/accounts/avatars/001/021/813/original/feeb19e419f0e3c4.jpg",
                                id="109761844504564708",
                                username="Some_Emo_Chick",
                                content="<p>The Onion never misses</p>",
                                media="https://files.mastodon.social/media_attachments/files/109/761/841/472/834/189/original/b79eebc4402ae01b.png",
                                post_time="2023-01-27T15:20:32.415Z",
                                replies_count=12,
                                reblogs_count=753,
                                favourites_count=1111))
    sample_post_data.append(Post(
                            profile_photo="https://files.mastodon.social/accounts/avatars/000/276/336/original/a2fc430ff065be26.jpg",
                            id="109762190140654574",
                            username="lizzard",
                            content="<p>Happy Large Boulder the Size of a Small Boulder Day! Please celebrate by posting pictures of rocks of indeterminate sizes or maybe your favorite boulder</p>",
                            media="https://files.mastodon.social/media_attachments/files/109/762/181/711/458/430/original/e0a3dec6cba76e3a.png",
                            post_time="2023-01-27T16:48:26.402Z",
                            replies_count=37,
                            reblogs_count=320,
                            favourites_count=432))

    parsed_posts = parse_posts(sample_posts_json)

    for i in range(len(sample_post_data)):
        assert parsed_posts[i].__dict__ == sample_post_data[i].__dict__
