from loguru import logger
from os import getenv
from dotenv import load_dotenv
from pyrogram import Client
from simpledigestlying.core.handlers import register_handlers

load_dotenv()

api_id: str | None = getenv("API_ID")
api_hash: str | None = getenv("API_HASH")

app = Client(
    "simpledigestlying",
    api_id=api_id,
    api_hash=api_hash,
)

register_handlers(app)

if __name__ == "__main__":
    logger.add(sink="../logs/app.log", level="INFO")
    app.run()
