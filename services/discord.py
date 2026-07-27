import os
import time
import requests

TEST_WEBHOOK = os.getenv("TEST_WEBHOOK")


def send_post(post):
    payload = {
        "content": (
            f"## {post.title}\n\n"
            f"**Game:** {post.game}\n"
            f"**Source:** {post.feed}\n"
            f"{post.url}"
        )
    }

    while True:
        try:
            response = requests.post(
                TEST_WEBHOOK,
                json=payload,
                timeout=20,
            )

            # Success
            if response.status_code in (200, 204):
                print(f"✅ Sent: {post.title}")

                # Small delay to avoid hitting Discord rate limits
                time.sleep(0.35)
                return

            # Discord rate limit
            if response.status_code == 429:
                data = response.json()

                retry_after = data.get("retry_after", 1)

                print(f"⏳ Discord rate limited. Retrying in {retry_after} seconds...")

                time.sleep(float(retry_after))

                continue

            # Other errors
            print(f"❌ Discord Error {response.status_code}")
            print(response.text)
            return

        except requests.RequestException as e:
            print(f"❌ Request Error: {e}")

            # Wait a bit before retrying network errors
            time.sleep(2)
