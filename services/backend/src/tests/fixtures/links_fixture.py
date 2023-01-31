from ...utilities.links_parser import Link


def expected_links_success():
    sample_links_data = []
    sample_links_data.append(Link(
        url="https://www.bloomberg.com/news/articles/2023-01-27/elon-musk-s-twitter-trust-safety-head-ella-irwin-breaks-rules-for-him",
        title="Twitter\u2019s Trust and Safety Head Ditches Protocol for Musk Whims",
        description="Ella Irwin is Musk\u2019s most faithful supporter, even when his impulses buck convention",
        author_name="Davey Alba",
        provider_name="Bloomberg",
        image="https://files.mastodon.social/cache/preview_cards/images/053/183/665/original/9f75b7cc707ab146.jpg",
        blurhash="UV8?g_adX=t8x^bIROjXa#fkoef5M{f6tRay")
    )
    sample_links_data.append(Link(
        url="https://www.houstonchronicle.com/business/article/twitter-mastadon-elon-musk-apps-migration-17746197.php",
        title="As Twitter kills third-party apps, new life blooms on Mastodon",
        description="Developers who crafted now-defunct apps for Twitter can devote their attention to the network that\u2019s become the primary bird site refuge.",
        author_name="Dwight Silverman",
        provider_name="Houston Chronicle",
        image="https://files.mastodon.social/cache/preview_cards/images/053/246/074/original/afe2b26bf6d4e269.jpg",
        blurhash="UKQ,OGM}xs?a~p%L9ZIV9GM{%Mxa-;t7M|M{"))
    return sample_links_data


def sample_links_json_success():
    return [
        {
            "url": "https://www.bloomberg.com/news/articles/2023-01-27/elon-musk-s-twitter-trust-safety-head-ella-irwin-breaks-rules-for-him",
            "title": "Twitter\u2019s Trust and Safety Head Ditches Protocol for Musk Whims",
            "description": "Ella Irwin is Musk\u2019s most faithful supporter, even when his impulses buck convention",
            "type": "link",
            "author_name": "Davey Alba",
            "author_url": "",
            "provider_name": "Bloomberg",
            "provider_url": "",
            "html": "",
            "width": 400,
            "height": 225,
            "image": "https://files.mastodon.social/cache/preview_cards/images/053/183/665/original/9f75b7cc707ab146.jpg",
            "embed_url": "",
            "blurhash": "UV8?g_adX=t8x^bIROjXa#fkoef5M{f6tRay",
            "history": [
                {
                    "day": "1674777600",
                    "accounts": "347",
                    "uses": "412"
                },
                {
                    "day": "1674691200",
                    "accounts": "0",
                    "uses": "0"
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
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674345600",
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674259200",
                    "accounts": "0",
                    "uses": "0"
                }
            ]
        },
        {
            "url": "https://www.houstonchronicle.com/business/article/twitter-mastadon-elon-musk-apps-migration-17746197.php",
            "title": "As Twitter kills third-party apps, new life blooms on Mastodon",
            "description": "Developers who crafted now-defunct apps for Twitter can devote their attention to the network that\u2019s become the primary bird site refuge.",
            "type": "link",
            "author_name": "Dwight Silverman",
            "author_url": "https://www.houstonchronicle.com/author/dwight-silverman/",
            "provider_name": "Houston Chronicle",
            "provider_url": "",
            "html": "",
            "width": 400,
            "height": 278,
            "image": "https://files.mastodon.social/cache/preview_cards/images/053/246/074/original/afe2b26bf6d4e269.jpg",
            "embed_url": "",
            "blurhash": "UKQ,OGM}xs?a~p%L9ZIV9GM{%Mxa-;t7M|M{",
            "history": [
                {
                    "day": "1674777600",
                    "accounts": "248",
                    "uses": "249"
                },
                {
                    "day": "1674691200",
                    "accounts": "0",
                    "uses": "0"
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
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674345600",
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674259200",
                    "accounts": "0",
                    "uses": "0"
                }
            ]
        }
    ]


def sample_links_json_fail():
    return [
        {
            "title": "Twitter\u2019s Trust and Safety Head Ditches Protocol for Musk Whims",
            "description": "Ella Irwin is Musk\u2019s most faithful supporter, even when his impulses buck convention",
            "type": "link",
            "author_name": "Davey Alba",
            "author_url": "",
            "provider_name": "Bloomberg",
            "provider_url": "",
            "html": "",
            "width": 400,
            "height": 225,
            "image": "https://files.mastodon.social/cache/preview_cards/images/053/183/665/original/9f75b7cc707ab146.jpg",
            "embed_url": "",
            "blurhash": "UV8?g_adX=t8x^bIROjXa#fkoef5M{f6tRay",
            "history": [
                {
                    "day": "1674777600",
                    "accounts": "347",
                    "uses": "412"
                },
                {
                    "day": "1674691200",
                    "accounts": "0",
                    "uses": "0"
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
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674345600",
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674259200",
                    "accounts": "0",
                    "uses": "0"
                }
            ]
        },
        {
            "url": "https://www.houstonchronicle.com/business/article/twitter-mastadon-elon-musk-apps-migration-17746197.php",
            "title": "As Twitter kills third-party apps, new life blooms on Mastodon",
            "description": "Developers who crafted now-defunct apps for Twitter can devote their attention to the network that\u2019s become the primary bird site refuge.",
            "type": "link",
            "author_name": "Dwight Silverman",
            "author_url": "https://www.houstonchronicle.com/author/dwight-silverman/",
            "provider_name": "Houston Chronicle",
            "provider_url": "",
            "html": "",
            "width": 400,
            "height": 278,
            "image": "https://files.mastodon.social/cache/preview_cards/images/053/246/074/original/afe2b26bf6d4e269.jpg",
            "embed_url": "",
            "blurhash": "UKQ,OGM}xs?a~p%L9ZIV9GM{%Mxa-;t7M|M{",
            "history": [
                {
                    "day": "1674777600",
                    "accounts": "248",
                    "uses": "249"
                },
                {
                    "day": "1674691200",
                    "accounts": "0",
                    "uses": "0"
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
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674345600",
                    "accounts": "0",
                    "uses": "0"
                },
                {
                    "day": "1674259200",
                    "accounts": "0",
                    "uses": "0"
                }
            ]
        }
    ]
