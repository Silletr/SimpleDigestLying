from aiogram import Dispatcher
from simpledigestlying.core.handlers import router as start_router

dispatcher = Dispatcher()
dispatcher.include_router(start_router)
