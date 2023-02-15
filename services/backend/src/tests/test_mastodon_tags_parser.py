from .fixtures.trends_fixture import sample_trends_json_fail, sample_trends_json_success
from src.utilities import MastodonTagsParser
from src.viewmodels import TrendViewModel
import pytest
from fastapi import HTTPException


def test_trends_parser_success():
    # arrange
    sample_trend_data = []
    sample_trend_data.append(TrendViewModel("Fensterfreitag"))
    sample_trend_data.append(TrendViewModel("WindowFriday"))
    trends_parser = MastodonTagsParser()

    # act
    parsed_trends = trends_parser.parse(sample_trends_json_success())

    # assert
    for i in range(len(sample_trend_data)):
        assert parsed_trends[i].__dict__ == sample_trend_data[i].__dict__


def test_trends_parser_fail():
    # arrange 
    trends_parser = MastodonTagsParser()

    #assert
    with pytest.raises(HTTPException):
        trends_parser.parse(sample_trends_json_fail())
