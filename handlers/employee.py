from aiogram import F, Router
from aiogram.types import CallbackQuery

from configs import delete_or_continue
from content.buttons import MainMenuButtons
from content.keyboards import employee_keyboard
from content.texts import EmployeeAnswers


router = Router()


@router.callback_query(F.data == MainMenuButtons.EMPLOYEE.value[1])
async def employee(callback: CallbackQuery):
    """Employee button handler."""
    name = callback.from_user.first_name
    await delete_or_continue(callback)
    await callback.message.answer(
        text=EmployeeAnswers.TEXT.format(name),
        reply_markup=employee_keyboard
    )
    await callback.answer()
