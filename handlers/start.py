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


# @router.message(F.photo)
# async def get_file_id(message: Message):
#     # Получаем file_id самой большой фотографии (лучшего качества)
#     file_id = message.photo[-1].file_id
#     spisok.append(file_id)
#     await message.answer(f"file_id: {spisok}")
