import os
import time
import requests
import feedparser

from config import REDDIT_SOURCES
from models.post import Post
from services.formatter import (
    format_reddit_url,
    is_youtube_link,
)

HEADERS = {
    "User-Agent": "PersonalBot/1.0 (+GitHub Actions)"
}


def fetch_posts():

    posts = []

    game_key = os.getenv("GAME")

    if not game_key:
        print("GAME environment variable not set.")
        return posts

    if game_key not in REDDIT_SOURCES:
        print(f"Unknown GAME: {game_key}")
        return posts

    source = REDDIT_SOURCES[game_key]

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
            return posts

        feed = feedparser.parse(response.text)

        if feed.bozo:
            print(f"RSS Parse Error: {feed.bozo_exception}")
            return posts

        print(f"Found {len(feed.entries)} entries")

        for entry in feed.entries:

            url = entry.link

            if is_youtube_link(url):
                continue

            post_id = getattr(entry, "id", url)
            author = getattr(entry, "author", "")
            published = getattr(entry, "published", "")

            thumbnail = ""

            if hasattr(entry, "media_thumbnail"):
                thumbnail = entry.media_thumbnail[0].get("url", "")

            content = ""
            if hasattr(entry, "content"):
                content = entry.content[0].value

            print("=" * 80)
            print(f"TITLE      : {entry.title}")
            print(f"AUTHOR     : {author}")
            print(f"PUBLISHED  : {published}")
            print(f"URL        : {url}")
            print(f"THUMBNAIL  : {thumbnail}")
            print("CONTENT PREVIEW:")
            print(content[:500])
            print("=" * 80)

            posts.append(
                Post(
                    id=post_id,
                    game=source["game"],
                    source="reddit",
                    feed=source["name"],
                    title=entry.title,
                    url=format_reddit_url(url),
                    published=published,
                    author=author,
                    thumbnail=thumbnail,
                )
            )

    except Exception as e:
        print(f"Request Error: {e}")

    time.sleep(1)

    print(f"\nCollected {len(posts)} Reddit posts.")

    return posts
