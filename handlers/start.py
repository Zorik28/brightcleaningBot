from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from configs import delete_or_continue
from content.buttons import TO_MAIN_MENU
from content.keyboards import start_keyboard
from content.texts import GREETING


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    """Start button handler."""
    await message.answer(text=GREETING, reply_markup=start_keyboard)


@router.callback_query(F.data == TO_MAIN_MENU[1])
async def to_main_menu(callback: CallbackQuery):
    """'to main menu' button handler."""
    await delete_or_continue(callback)
    await callback.message.answer(text=GREETING, reply_markup=start_keyboard)
    await callback.answer()


# # Обработчик всех типов сообщений
# @router.message()
# async def handle_docs(message: Message):
#     document = message.video
#     file_id = document.file_id
#     await message.reply(f"File ID: {file_id}")
