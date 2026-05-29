from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime
from zoneinfo import ZoneInfo
from loguru import logger
import tracemalloc

tracemalloc.start()
#    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#    ┃    get messages from the last 24h    ┃
#    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
today = datetime.now(tz=ZoneInfo("Europe/Kyiv"))
logger.add(
    sink="../logs/handlers.py.log",
    level="INFO",
    format="{time:DD/MM/YYYY HH:mm:ss} | {level} | {message}",
)


def register_handlers(app: Client):
    @app.on_message(filters.command("start") & filters.private)
    async def start_handler(client: Client, message: Message):
        await message.reply("Hi. I am alive.")

    @app.on_message(filters.command("history") & filters.private)
    async def history_handler(client: Client, message: Message):
        async for msg in app.get_chat_history(
            chat_id=message.chat.id, offset_date=today
        ):
            logger.success(
                f"Message text: {msg.text} | Message sender: {
                    msg.from_user.username if msg.from_user else 'unknown'
                }"
            )

        await client.send_message(
            chat_id=message.chat.id,
            text="Successfully sent history to the ../logs/handlers.py.log. Check it out right fcking now",
        )
