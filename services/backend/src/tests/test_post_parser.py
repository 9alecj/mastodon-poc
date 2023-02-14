from .fixtures.posts_fixture import expected_posts_success, sample_posts_json_fail, sample_posts_json_success
from src.utilities import PostsParser
import pytest
from fastapi import HTTPException


def test_post_parser_success():
    # arrange
    expected = expected_posts_success()
    posts_parser = PostsParser()

    # act
    parsed_posts = posts_parser.parse(sample_posts_json_success())

    # assert
    for i in range(len(expected)):
        assert parsed_posts[i].__dict__ == expected[i].__dict__


def test_post_parser_fail():
    # arrange 
    posts_parser = PostsParser()

    # assert
    with pytest.raises(HTTPException):
        posts_parser.parse(sample_posts_json_fail())
