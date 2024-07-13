from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from content.buttons import MainButtons
from content.keyboards import start_keyboard
from content.texts import CHECK_LIST, GREETING


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    """Start button handler."""
    await message.answer(text=GREETING, reply_markup=start_keyboard)


@router.callback_query(F.data == MainButtons.SUPPORT.value[1])
async def support(callback: CallbackQuery):
    """Support button handler."""
    await callback.message.answer_document(document=CHECK_LIST)
    await callback.answer()


# # Обработчик всех типов сообщений
# @router.message()
# async def handle_docs(message: Message):
#     document = message.document
#     file_id = document.file_id
#     await message.reply(f"File ID: {file_id}")
