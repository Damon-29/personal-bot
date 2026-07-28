import requests
import feedparser

# RSSHub test
RSS_URL = "https://rsshub.app/twitter/user/Wuthering_Waves"

HEADERS = {
    "User-Agent": "PersonalBot/1.0 (+GitHub Actions)"
}

print("Checking Wuthering_Waves...")

try:
    response = requests.get(
        RSS_URL,
        headers=HEADERS,
        timeout=20,
    )

    print("HTTP Status:", response.status_code)

    if response.status_code != 200:
        print(response.text[:500])
        exit()

    feed = feedparser.parse(response.text)

    if feed.bozo:
        print("RSS Parse Error:", feed.bozo_exception)

    print(f"Found {len(feed.entries)} entries\n")

    for entry in feed.entries[:5]:
        print("=" * 80)
        print("TITLE     :", entry.title)
        print("LINK      :", entry.link)
        print("PUBLISHED :", getattr(entry, "published", ""))
        print("=" * 80)

except Exception as e:
    print("Request Error:", e)
