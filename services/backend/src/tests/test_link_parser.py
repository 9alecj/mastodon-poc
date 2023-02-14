from .fixtures.links_fixture import expected_links_success, sample_links_json_fail, sample_links_json_success
from src.utilities import LinksParser
import pytest
from fastapi import HTTPException


def test_link_parser_success():
    # arrange
    expected = expected_links_success()
    links_parser = LinksParser()

    # act
    parsed_links = links_parser.parse(sample_links_json_success())

    # assert
    for i in range(len(expected)):
        assert parsed_links[i].__dict__ == expected[i].__dict__


def test_link_parser_fail():
    # arrange
    links_parser = LinksParser()

    # assert
    with pytest.raises(HTTPException):
        links_parser.parse(sample_links_json_fail())
