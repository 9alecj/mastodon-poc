from .fixtures.microblog_posts_fixture import expected_posts_success, sample_posts_json_success, sample_posts_json_fail
from src.utilities import MicroblogPostsParser
import pytest
from fastapi import HTTPException


def test_post_parser_success():
    # arrange
    expected = expected_posts_success()
    posts_parser = MicroblogPostsParser()

    # act
    parsed_posts = posts_parser.parse(sample_posts_json_success())

    # assert
    for i in range(len(expected)):
        print(parsed_posts[i].__dict__)
        print(expected[i].__dict__)
        assert parsed_posts[i].__dict__ == expected[i].__dict__


def test_post_parser_fail():
    # arrange 
    posts_parser = MicroblogPostsParser()

    # assert
    with pytest.raises(HTTPException):
        posts_parser.parse(sample_posts_json_fail())
