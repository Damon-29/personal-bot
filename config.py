import os

TEST_WEBHOOK = os.getenv("TEST_WEBHOOK")

REDDIT_SOURCES = {
    "wuwa": {
        "game": "Wuthering Waves",
        "name": "WutheringWaves",
        "rss": "https://www.reddit.com/r/WutheringWaves/.rss",
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

YOUTUBE_SOURCES = {
    "wuwa": [
        {
            "game": "Wuthering Waves",
            "name": "Wuthering Waves",
            "rss": "https://www.youtube.com/feeds/videos.xml?channel_id=UC0Bi5KMcECRVYis5Gb_ZYZQ",
        }
    ],

    "genshin": [
        {
            "game": "Genshin Impact",
            "name": "Genshin Impact",
            "rss": "https://www.youtube.com/feeds/videos.xml?channel_id=UCiS882YPwZt1NfaM0gR0D9Q",
        }
    ],

    "zzz": [
        {
            "game": "Zenless Zone Zero",
            "name": "Zenless Zone Zero",
            "rss": "https://www.youtube.com/feeds/videos.xml?channel_id=UC2SpC8rL9LaeQriE4YNdyzA",
        }
    ],

    "hsr": [
        {
            "game": "Honkai: Star Rail",
            "name": "Honkai: Star Rail",
            "rss": "https://www.youtube.com/feeds/videos.xml?channel_id=UC2PeMPA8PAOp-bynLoCeMLA",
        }
    ],
}
