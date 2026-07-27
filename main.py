from modules.reddit import fetch_posts

posts = fetch_posts()

print(f"Found {len(posts)} posts")

for post in posts[:5]:
    print(post.title)
