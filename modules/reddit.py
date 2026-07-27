import feedparser

from config import REDDIT_SOURCES
from models.post import Post
from services.formatter import (
    format_reddit_url,
    is_youtube_link,
)


def fetch_posts():

    posts = []

    for source in REDDIT_SOURCES:

        print(f"\nChecking {source['name']}...")

        feed = feedparser.parse(source["rss"])

        if feed.bozo:
            print(f"RSS Error: {feed.bozo_exception}")
            continue

        print(f"Found {len(feed.entries)} entries")

        for entry in feed.entries:

            url = entry.link

            if is_youtube_link(url):
                continue

            # Stable unique ID from RSS
            post_id = getattr(entry, "id", url)

            author = getattr(entry, "author", "")

            published = getattr(entry, "published", "")

            thumbnail = ""

            if hasattr(entry, "media_thumbnail"):
                thumbnail = entry.media_thumbnail[0].get("url", "")

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

    print(f"\nCollected {len(posts)} Reddit posts.")

    return posts
