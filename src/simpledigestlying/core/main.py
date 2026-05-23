import asyncio
from loguru import logger
from os import getenv
from dotenv import load_dotenv
from pyrogram import Client
from simpledigestlying.core.handlers import register_handlers

load_dotenv()

app = Client(
    "simpledigestlying",
    api_id=getenv("API_ID"),
    api_hash=getenv("API_HASH"),
)

register_handlers(app)

if __name__ == "__main__":
    logger.add(sink="../logs/app.log", level="INFO")
    app.run()
