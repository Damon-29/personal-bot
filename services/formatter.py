from urllib.parse import urlparse


def format_reddit_url(url: str) -> str:
    """
    Convert reddit.com links to vxreddit.com.
    """
    return url.replace("reddit.com", "vxreddit.com")


def format_twitter_url(url: str) -> str:
    """
    Convert x.com links to fxtwitter.com.
    """
    return (
        url.replace("x.com", "fxtwitter.com")
           .replace("twitter.com", "fxtwitter.com")
    )


def is_youtube_link(url: str) -> bool:
    """
    Check if a URL points to YouTube.
    """
    hostname = urlparse(url).netloc.lower()

    return (
        "youtube.com" in hostname
        or "youtu.be" in hostname
    )
