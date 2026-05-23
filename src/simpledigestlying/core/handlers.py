from pyrogram import Client, filters
from pyrogram.types import Message


def register_handlers(app: Client):
    @app.on_message(filters.command("start") & filters.private)
    async def start_handler(client: Client, message: Message):
        await message.reply("Hi. I am alive.")
