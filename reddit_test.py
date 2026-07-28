import requests

url = "https://www.reddit.com/r/WutheringWaves/new.json?limit=5"

headers = {
    "User-Agent": "WuWaNewsBot/1.0"
}

r = requests.get(url, headers=headers, timeout=15)

print("Status:", r.status_code)
print(r.text[:500])
