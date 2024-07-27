from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from content.keyboards import start_keyboard
from content.texts import GREETING


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    """Start button handler."""
    await message.answer(text=GREETING, reply_markup=start_keyboard)


# # Обработчик всех типов сообщений
# @router.message()
# async def handle_docs(message: Message):
#     document = message.video
#     file_id = document.file_id
#     await message.reply(f"File ID: {file_id}")
