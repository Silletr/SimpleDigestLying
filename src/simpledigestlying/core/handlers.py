from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

#    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#    ┃    get messages from the last 24h    ┃
#    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
today = datetime.now(tz=ZoneInfo("Europe/Kyiv"))


def register_handlers(app: Client):
    @app.on_message(filters.command("start") & filters.private)
    async def start_handler(client: Client, message: Message):
        await message.reply("Hi. I am alive.")

    @app.on_message(filters.command("history") & filters.private)
    async def history_handler(client: Client, message: Message):
        today = datetime.now(tz=ZoneInfo("Europe/Kyiv"))
        async for msg in app.get_chat_history(chat_id="me", offset_date=today):
            print(msg.text)
