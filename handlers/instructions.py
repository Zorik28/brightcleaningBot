from aiogram import F, Router
from aiogram.types import CallbackQuery, InputMediaPhoto

from configs import delete_or_continue
from content.buttons import InstructionsButtons, MainMenuButtons
from content.keyboards import instructions_keyboard
from content.texts import InstructionAnswers


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


@router.callback_query(F.data == InstructionsButtons.AIRBNB.value[1])
async def airbnb(callback: CallbackQuery):
    """Airbnb button handler."""
    # Создает список InputMediaPhoto на основе переданных file_id
    media_1 = [InputMediaPhoto(media=file_id) for file_id in InstructionAnswers.AIRBNB_PHOTOS_1.value]
    media_2 = [InputMediaPhoto(media=file_id) for file_id in InstructionAnswers.AIRBNB_PHOTOS_2.value]
    await callback.message.answer_media_group(media=media_1)
    await callback.message.answer_media_group(media=media_2)
    await callback.answer()
