from .fixtures.trends_fixture import sample_trends_json
from ..main import app
from ..utilities.trends_parser import Trend, parse_trends
import pytest

def test_read_main(sample_trends_json):
    sample_trend_data = []
    sample_trend_data.append(Trend("Fensterfreitag"))
    sample_trend_data.append(Trend("WindowFriday"))
    parsed_trends = parse_trends(sample_trends_json)

    for i in range(len(sample_trend_data)):
        assert parsed_trends[i].__dict__ == sample_trend_data[i].__dict__

