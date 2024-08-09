from aiogram import F, Router
from aiogram.types import CallbackQuery

from configs import delete_or_continue
from content.buttons import MainMenuButtons
from content.keyboards import support_keyboard
from content.texts import SUPPORT


router = Router()


@router.callback_query(F.data == MainMenuButtons.SUPPORT.value[1])
async def support(callback: CallbackQuery):
    """Support button handler."""
    await delete_or_continue(callback)
    await callback.message.answer(
        text=SUPPORT, reply_markup=support_keyboard
    )
    await callback.answer()
