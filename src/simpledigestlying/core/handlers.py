from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime
from zoneinfo import ZoneInfo
from loguru import logger
import tracemalloc

tracemalloc.start()

kyiv = ZoneInfo("Europe/Kyiv")
today = datetime.now(tz=kyiv)

logger.add(
    sink="../logs/handlers.py.log",
    level="INFO",
    format="{time:DD/MM/YYYY HH:mm:ss} | {level} | {message}",
)


#  ────────────────────────────────────────────────────────────────
def register_handlers(app: Client):
    @app.on_message(filters.command("start") & filters.private)
    async def start_handler(client: Client, message: Message):
        await message.reply("Hi. I am alive.")

    @app.on_message(filters.command("history") & filters.private)
    async def history_handler(client: Client, message: Message):
        async for msg in app.get_chat_history(
            chat_id=message.chat.id, offset_date=today
        ):
            msg_date_kyiv = msg.date.replace(tzinfo=ZoneInfo("UTC")).astimezone(kyiv)
            if msg_date_kyiv.date() == today.date():
                logger.success(
                    f"Message text: {msg.text} | "
                    f"Message sender: {
                        msg.from_user.username if msg.from_user else 'unknown'
                    }"
                )
                with open("chat_history.txt", mode="a") as file:
                    file.write(
                        f"Message Sender: {
                            msg.from_user.username if msg.from_user else 'No Name'
                        }\n"
                        f"Message Text: {msg.text}\n"
                    )
            else:
                break
        await client.send_message(
            chat_id=message.chat.id, text="Successfully saved to `logs/handlers.py.log`"
        )
