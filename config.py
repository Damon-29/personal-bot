import os

TEST_WEBHOOK = os.getenv("TEST_WEBHOOK")

REDDIT_SOURCES = {
    "wuwa": {
        "game": "Wuthering Waves",
        "name": "WutheringWavesLeaks",
        "rss": "https://www.reddit.com/r/WutheringWavesLeaks/new/.rss",
    },
    "genshin": {
        "game": "Genshin Impact",
        "name": "Genshin_Impact_Leaks",
        "rss": "https://www.reddit.com/r/Genshin_Impact_Leaks/new/.rss",
    },
    "zzz": {
        "game": "Zenless Zone Zero",
        "name": "Zenlesszonezeroleaks_",
        "rss": "https://www.reddit.com/r/Zenlesszonezeroleaks_/new/.rss",
    },
    "hsr": {
        "game": "Honkai: Star Rail",
        "name": "HonkaiStarRail_leaks",
        "rss": "https://www.reddit.com/r/HonkaiStarRail_leaks/new/.rss",
    },
}
