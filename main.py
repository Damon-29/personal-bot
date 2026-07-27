from modules.reddit import fetch_posts

posts = fetch_posts()

print(f"Found {len(posts)} posts")

for post in posts[:5]:
    print(post.title)
from modules.reddit import fetch_posts
from services.state import (
    load_state,
    save_state,
    is_seen,
    mark_seen
)
from services.discord import send_post


def main():
    state = load_state()

    posts = fetch_posts()

    for post in posts:

        if is_seen(state, "reddit", post.id, post.id):
            continue

        send_post(post)

        mark_seen(state, "reddit", post.id, post.id)

    save_state(state)


if __name__ == "__main__":
    main()
