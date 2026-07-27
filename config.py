import os

TEST_WEBHOOK = os.getenv("TEST_WEBHOOK")

CHECK_INTERVAL = 300

REDDIT_SOURCES = [

    # =======================
    # Wuthering Waves
    # =======================

    {
        "game": "wuwa",
        "name": "WutheringWaves",
        "rss": "https://www.reddit.com/r/WutheringWaves/new/.rss",
    },
    {
        "game": "wuwa",
        "name": "WutheringWavesLeaks",
        "rss": "https://www.reddit.com/r/WutheringWavesLeaks/new/.rss",
    },

    # =======================
    # Genshin
    # =======================

    {
        "game": "genshin",
        "name": "Genshin_Impact",
        "rss": "https://www.reddit.com/r/Genshin_Impact/new/.rss",
    },
    {
        "game": "genshin",
        "name": "Genshin_Impact_Leaks",
        "rss": "https://www.reddit.com/r/Genshin_Impact_Leaks/new/.rss",
    },

    # =======================
    # ZZZ
    # =======================

    {
        "game": "zzz",
        "name": "ZZZ_Official",
        "rss": "https://www.reddit.com/r/ZZZ_Official/new/.rss",
    },
    {
        "game": "zzz",
        "name": "Zenlesszonezeroleaks_",
        "rss": "https://www.reddit.com/r/Zenlesszonezeroleaks_/new/.rss",
    },

    # =======================
    # HSR
    # =======================

    {
        "game": "hsr",
        "name": "HonkaiStarRail",
        "rss": "https://www.reddit.com/r/HonkaiStarRail/new/.rss",
    },
    {
        "game": "hsr",
        "name": "HonkaiStarRail_leaks",
        "rss": "https://www.reddit.com/r/HonkaiStarRail_leaks/new/.rss",
    },
]
