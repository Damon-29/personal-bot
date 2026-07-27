import json
from pathlib import Path

STATE_FILE = Path("data/state.json")

MAX_IDS_PER_FEED = 100


def load_state():
    if not STATE_FILE.exists():
        return {
            "reddit": {},
            "youtube": {},
            "twitter": {}
        }

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4)


def is_seen(state, source, feed, post_id):
    return post_id in state.get(source, {}).get(feed, [])


def mark_seen(state, source, feed, post_id):
    state.setdefault(source, {})
    state[source].setdefault(feed, [])

    if post_id not in state[source][feed]:
        state[source][feed].append(post_id)

    # Keep only the latest 100 IDs
    state[source][feed] = state[source][feed][-MAX_IDS_PER_FEED:]
