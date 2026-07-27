from modules.registry import load_modules
from services.state import (
    load_state,
    save_state,
    is_seen,
    mark_seen,
)
from services.discord import send_post


def main():
    state = load_state()

    modules = load_modules()

    for module in modules:

        posts = module.fetch_posts()

        for post in posts:

            if is_seen(state, post.source, post.feed, post.id):
                continue

            send_post(post)

            mark_seen(
                state,
                post.source,
                post.feed,
                post.id,
            )

    save_state(state)


if __name__ == "__main__":
    main()
