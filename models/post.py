from dataclasses import dataclass


@dataclass
class Post:
    id: str
    game: str
    source: str

    title: str
    url: str

    published: str

    author: str = ""
    thumbnail: str = ""
