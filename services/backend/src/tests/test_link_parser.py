from .fixtures.links_fixture import expected_links_success, sample_links_json_fail, sample_links_json_success
from ..utilities.link_parser import parse_links
import pytest
from fastapi import HTTPException


def test_link_parser_success():
    # arrange
    expected = expected_links_success()

    # act
    parsed_links = parse_links(sample_links_json_success())

    # assert
    for i in range(len(expected)):
        assert parsed_links[i].__dict__ == expected[i].__dict__


def test_link_parser_fail():
    with pytest.raises(HTTPException):
        parse_links(sample_links_json_fail())
