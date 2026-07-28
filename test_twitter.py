import requests
import feedparser

RSS_URL = "https://nitter.poast.org/Wuthering_Waves/rss"

HEADERS = {
    "User-Agent": "PersonalBot/1.0 (+GitHub Actions)"
}

print("Checking Wuthering_Waves...")

response = requests.get(
    RSS_URL,
    headers=HEADERS,
    timeout=20,
)

print("HTTP Status:", response.status_code)

if response.status_code == 200:
    feed = feedparser.parse(response.text)

    print("Found", len(feed.entries), "entries\n")

    for entry in feed.entries[:5]:
        print("=" * 80)
        print("TITLE     :", entry.title)
        print("LINK      :", entry.link)
        print("PUBLISHED :", getattr(entry, "published", ""))
        print("=" * 80)
else:
    print(response.text[:500])
