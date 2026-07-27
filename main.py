import os
import requests

webhook = os.getenv("TEST_WEBHOOK")

payload = {
    "content": "✅ Personal Bot is running from GitHub Actions!"
}

response = requests.post(webhook, json=payload)

print(response.status_code)
print(response.text)
