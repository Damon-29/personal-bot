from models.post import Post
from services.discord import send_post


post = Post(
    id="1",
    game="wuwa",
    source="test",
    title="Hello Discord!",
    url="https://google.com",
    published="today"
)

send_post(post)
