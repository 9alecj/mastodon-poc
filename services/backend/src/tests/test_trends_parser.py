from .fixtures.trends_fixture import sample_trends_json_fail, sample_trends_json_success
from ..utilities.trends_parser import Trend, parse_trends
import pytest
from fastapi import HTTPException

def test_trends_parser_success():
    #arrange
    sample_trend_data = []
    sample_trend_data.append(Trend("Fensterfreitag"))
    sample_trend_data.append(Trend("WindowFriday"))

    #act
    parsed_trends = parse_trends(sample_trends_json_success())

    #assert
    for i in range(len(sample_trend_data)):
        assert parsed_trends[i].__dict__ == sample_trend_data[i].__dict__

def test_trends_parser_fail():
    with pytest.raises(HTTPException):
        parse_trends(sample_trends_json_fail())

