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
        "url": "https://www.reddit.com/r/WutheringWaves/new.json?limit=25",
        "allowed_flairs": ["Official News"]
    },
    {
        "game": "wuwa",
        "name": "WutheringWavesLeaks",
        "url": "https://www.reddit.com/r/WutheringWavesLeaks/new.json?limit=25",
        "allowed_flairs": []
    },

    # =======================
    # Genshin Impact
    # =======================

    {
        "game": "genshin",
        "name": "Genshin_Impact",
        "url": "https://www.reddit.com/r/Genshin_Impact/new.json?limit=25",
        "allowed_flairs": ["Official Post"]
    },
    {
        "game": "genshin",
        "name": "Genshin_Impact_Leaks",
        "url": "https://www.reddit.com/r/Genshin_Impact_Leaks/new.json?limit=25",
        "allowed_flairs": []
    },

    # =======================
    # Zenless Zone Zero
    # =======================

    {
        "game": "zzz",
        "name": "ZZZ_Official",
        "url": "https://www.reddit.com/r/ZZZ_Official/new.json?limit=25",
        "allowed_flairs": ["Official Media"]
    },
    {
        "game": "zzz",
        "name": "Zenlesszonezeroleaks_",
        "url": "https://www.reddit.com/r/Zenlesszonezeroleaks_/new.json?limit=25",
        "allowed_flairs": []
    },

    # =======================
    # Honkai Star Rail
    # =======================

    {
        "game": "hsr",
        "name": "HonkaiStarRail",
        "url": "https://www.reddit.com/r/HonkaiStarRail/new.json?limit=25",
        "allowed_flairs": ["Official Announcement"]
    },
    {
        "game": "hsr",
        "name": "HonkaiStarRail_leaks",
        "url": "https://www.reddit.com/r/HonkaiStarRail_leaks/new.json?limit=25",
        "allowed_flairs": []
    }

]
