import asyncio
from loguru import logger
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from simpledigestlying.core.dispatcher import dispatcher


#  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
async def main():
    load_dotenv()
    token = getenv("BOT_TOKEN")
    bot = Bot(
        token=token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logger.add(sink="../logs/app.log", level="INFO")
    asyncio.run(main())
