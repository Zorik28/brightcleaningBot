import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionMiddleware
from dotenv import load_dotenv

from handlers import routers


load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(storage=MemoryStorage())
dp.message.middleware(ChatActionMiddleware())

for router in routers:
    dp.include_router(router)

logging.basicConfig(
    level=logging.INFO,
    filename='bot_log.log',
    format='%(asctime)s %(levelname)s %(message)s'
)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
