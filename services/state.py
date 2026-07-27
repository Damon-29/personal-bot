import json
from pathlib import Path

STATE_FILE = Path("data/state.json")


def load_state():
    """Load state.json into memory."""
    if not STATE_FILE.exists():
        return {
            "reddit": {},
            "youtube": {},
            "twitter": {}
        }

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state):
    """Save the current state to state.json."""
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4)


def is_seen(state, source, feed, post_id):
    """
    Check whether a post has already been processed.
    """
    return post_id in state[source].get(feed, [])


def mark_seen(state, source, feed, post_id):
    """
    Mark a post as processed.
    """
    state[source].setdefault(feed, []).append(post_id)
