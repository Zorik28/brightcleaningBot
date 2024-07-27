from aiogram import F, Router
from aiogram.types import CallbackQuery

from configs import delete_or_continue
from content.buttons import InstructionsButtons, MainMenuButtons
from content.keyboards import instructions_keyboard, start_keyboard
from content.texts import GREETING, InstructionAnswers


router = Router()


@router.callback_query(F.data == MainMenuButtons.INSTRUCTIONS.value[1])
async def instructions(callback: CallbackQuery):
    """Instructions button handler."""
    await delete_or_continue(callback)
    await callback.message.answer(
        text=InstructionAnswers.TEXT,
        reply_markup=instructions_keyboard
    )
    await callback.answer()


@router.callback_query(F.data == InstructionsButtons.TO_MAIN_MENU.value[1])
async def to_main_menu(callback: CallbackQuery):
    """'to main menu' button handler."""
    await delete_or_continue(callback)
    await callback.message.answer(text=GREETING, reply_markup=start_keyboard)
    await callback.answer()


@router.callback_query(F.data == InstructionsButtons.FILE.value[1])
async def check_list(callback: CallbackQuery):
    """Check list button handler."""
    await callback.message.answer_document(
        document=InstructionAnswers.CHECK_LIST_PDF,
        caption="Пожалуйста, внимательно изучи чек-лист!"
    )
    await callback.answer()


@router.callback_query(F.data == InstructionsButtons.VIDEO.value[1])
async def video(callback: CallbackQuery):
    """Video button handler."""
    await callback.message.answer_video(
        video=InstructionAnswers.VIDEO_INSTRUCTION_MOV,
        caption="Видео инструкция к вашим услугам!"
    )
    await callback.answer()
