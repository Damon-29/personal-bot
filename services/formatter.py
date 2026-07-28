from urllib.parse import urlparse


def format_reddit_url(url: str) -> str:
    """
    Keep original Reddit URL.
    Discord now embeds reddit.com correctly.
    """
    return url


def format_twitter_url(url: str) -> str:
    """
    Keep original X/Twitter URL.
    Discord now embeds x.com correctly.
    """
    return url


def is_youtube_link(url: str) -> bool:
    """
    Check if a URL points to YouTube.
    """
    hostname = urlparse(url).netloc.lower()

    return (
        "youtube.com" in hostname
        or "youtu.be" in hostname
    )
