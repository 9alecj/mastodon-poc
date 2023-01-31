from .fixtures.posts_fixture import expected_posts_success, sample_posts_json_fail, sample_posts_json_success
from ..utilities.posts_parser import parse_posts
import pytest
from fastapi import HTTPException

def test_post_parser_success():
    #arrange
    expected = expected_posts_success()

    #act
    parsed_posts = parse_posts(sample_posts_json_success())
    
    #assert
    for i in range(len(expected)):
        assert parsed_posts[i].__dict__ == expected[i].__dict__

def test_post_parser_fail():
    with pytest.raises(HTTPException):
        parse_posts(sample_posts_json_fail())