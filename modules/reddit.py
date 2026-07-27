import requests

from config import REDDIT_SOURCES
from models.post import Post
from services.formatter import (
    format_reddit_url,
    is_youtube_link,
)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) PersonalBot/1.0"
}


def fetch_posts():
    posts = []

    for source in REDDIT_SOURCES:

        print(f"\nChecking {source['name']}...")

        try:
            response = requests.get(
                source["url"],
                headers=HEADERS,
                timeout=20,
            )

            print(f"Status Code: {response.status_code}")

            if response.status_code != 200:
                print("Response:")
                print(response.text[:500])
                continue

            data = response.json()

            children = data.get("data", {}).get("children", [])

            print(f"Found {len(children)} posts")

            for child in children:

                post = child["data"]

                flair = post.get("link_flair_text") or ""

                if (
                    source["allowed_flairs"]
                    and flair not in source["allowed_flairs"]
                ):
                    continue

                url = post.get("url", "")

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
                        published=str(post["created_utc"]),
                        author=post.get("author", ""),
                        thumbnail=post.get("thumbnail", ""),
                    )
                )

        except Exception as e:
            print(f"Error while checking {source['name']}")
            print(type(e).__name__)
            print(e)

    print(f"\nTotal Reddit posts collected: {len(posts)}")

    return posts
