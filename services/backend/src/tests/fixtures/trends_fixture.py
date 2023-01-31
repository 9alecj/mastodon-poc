import pytest

def sample_trends_json_success():
    return [
        {
            "name": "Fensterfreitag",
            "url": "https://mastodon.social/tags/fensterfreitag",
            "history": [
                {
                    "day": "1674777600",
                    "accounts": "401",
                    "uses": "468"
                },
                {
                    "day": "1674691200",
                    "accounts": "5",
                    "uses": "5"
                },
                {
                    "day": "1674604800",
                    "accounts": "4",
                    "uses": "4"
                },
                {
                    "day": "1674518400",
                    "accounts": "2",
                    "uses": "2"
                },
                {
                    "day": "1674432000",
                    "accounts": "2",
                    "uses": "2"
                },
                {
                    "day": "1674345600",
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674259200",
                    "accounts": "30",
                    "uses": "32"
                }
            ]
        },
        {
            "name": "WindowFriday",
            "url": "https://mastodon.social/tags/windowfriday",
            "history": [
                {
                    "day": "1674777600",
                    "accounts": "189",
                    "uses": "215"
                },
                {
                    "day": "1674691200",
                    "accounts": "3",
                    "uses": "3"
                },
                {
                    "day": "1674604800",
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674518400",
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674432000",
                    "accounts": "1",
                    "uses": "1"
                },
                {
                    "day": "1674345600",
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674259200",
                    "accounts": "38",
                    "uses": "40"
                }
            ]
        }
    ]

def sample_trends_json_fail():
    return [
        {
            "url": "https://mastodon.social/tags/fensterfreitag",
            "history": [
                {
                    "day": "1674777600",
                    "accounts": "401",
                    "uses": "468"
                },
                {
                    "day": "1674691200",
                    "accounts": "5",
                    "uses": "5"
                },
                {
                    "day": "1674604800",
                    "accounts": "4",
                    "uses": "4"
                },
                {
                    "day": "1674518400",
                    "accounts": "2",
                    "uses": "2"
                },
                {
                    "day": "1674432000",
                    "accounts": "2",
                    "uses": "2"
                },
                {
                    "day": "1674345600",
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674259200",
                    "accounts": "30",
                    "uses": "32"
                }
            ]
        },
        {
            "name": "WindowFriday",
            "url": "https://mastodon.social/tags/windowfriday",
            "history": [
                {
                    "day": "1674777600",
                    "accounts": "189",
                    "uses": "215"
                },
                {
                    "day": "1674691200",
                    "accounts": "3",
                    "uses": "3"
                },
                {
                    "day": "1674604800",
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674518400",
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674432000",
                    "accounts": "1",
                    "uses": "1"
                },
                {
                    "day": "1674345600",
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674259200",
                    "accounts": "38",
                    "uses": "40"
                }
            ]
        }
    ]