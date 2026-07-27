
import os
import time
import requests
import feedparser

from config import YOUTUBE_SOURCES
from models.post import Post

HEADERS = {
    "User-Agent": "PersonalBot/1.0 (+GitHub Actions)"
}


def fetch_posts():
    posts = []

    game_key = os.getenv("GAME")

    if not game_key:
        print("GAME environment variable not set.")
        return posts

    if game_key not in YOUTUBE_SOURCES:
        print(f"Unknown GAME: {game_key}")
        return posts

    print("\n========== YouTube ==========")

    for source in YOUTUBE_SOURCES[game_key]:

        print(f"\nChecking {source['name']}...")

        try:
            response = requests.get(
                source["rss"],
                headers=HEADERS,
                timeout=20,
            )

            print(f"HTTP Status: {response.status_code}")

            if response.status_code != 200:
                print("Failed to fetch RSS.")
                continue

            feed = feedparser.parse(response.text)

            if feed.bozo:
                print(f"RSS Parse Error: {feed.bozo_exception}")
                continue

            print(f"Found {len(feed.entries)} entries")

            for entry in feed.entries:

                url = entry.link

                # Basic Shorts filter
                if "/shorts/" in url:
                    continue

                thumbnail = ""

                if hasattr(entry, "media_thumbnail"):
                    thumbnail = entry.media_thumbnail[0].get("url", "")

                author = getattr(entry, "author", source["name"])
                published = getattr(entry, "published", "")
                post_id = getattr(entry, "id", url)

                posts.append(
                    Post(
                        id=post_id,
                        game=source["game"],
                        source="youtube",
                        feed=source["name"],
                        title=entry.title,
                        url=url,
                        published=published,
                        author=author,
                        thumbnail=thumbnail,
                    )
                )

        except Exception as e:
            print(f"Request Error: {e}")

        time.sleep(1)

    print(f"\nCollected {len(posts)} YouTube posts.")

    return posts
