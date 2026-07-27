import requests
from config import TEST_WEBHOOK


def send_post(post):
    """
    Send a Post object to Discord.
    """

    if not TEST_WEBHOOK:
        print("❌ TEST_WEBHOOK is not configured.")
        return

    payload = {
        "content": (
            f"## {post.title}\n\n"
            f"**Game:** {post.game.upper()}\n"
            f"**Source:** {post.source.upper()}\n"
            f"{post.url}"
        )
    }

    response = requests.post(TEST_WEBHOOK, json=payload)

    if response.status_code in (200, 204):
        print(f"✅ Sent: {post.title}")
    else:
        print(f"❌ Discord Error {response.status_code}")
        print(response.text)
