import requests

from config import REDDIT_SOURCES
from models.post import Post
from services.formatter import (
    format_reddit_url,
    is_youtube_link
)


HEADERS = {
    "User-Agent": "personal-bot/1.0"
}


def fetch_posts():

    posts = []

    for source in REDDIT_SOURCES:

        response = requests.get(
            source["url"],
            headers=HEADERS,
            timeout=15
        )

        if response.status_code != 200:
            print(f"Failed: {source['name']}")
            continue

        data = response.json()

        for child in data["data"]["children"]:

            post = child["data"]

            flair = post.get("link_flair_text") or ""

            if (
                source["allowed_flairs"]
                and flair not in source["allowed_flairs"]
            ):
                continue

            url = post["url"]

            if is_youtube_link(url):
                continue

            posts.append(
                Post(
                    id=post["id"],
                    game=source["game"],
                    source="reddit",
                    feed=source["name"],
                    title=post["title"],
                    url=format_reddit_url(post["permalink"]),
                    published=str(post["created_utc"])
                )
            )

    return posts
