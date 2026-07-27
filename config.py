import os

TEST_WEBHOOK = os.getenv("TEST_WEBHOOK")

REDDIT_SOURCES = [
    {
        "game": "wuwa",
        "name": "WutheringWaves",
        "url": "https://www.reddit.com/r/WutheringWaves/.json",
        "allowed_flairs": [
            "Official News"
        ]
    },
    {
        "game": "wuwa",
        "name": "WutheringWavesLeaks",
        "url": "https://www.reddit.com/r/WutheringWavesLeaks/.json",
        "allowed_flairs": []
    },
]
