from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from content.buttons import MainMenuButtons
from content.keyboards import start_keyboard
from content.texts import GREETING, InstructionAnswers


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    """Start button handler."""
    await message.answer(text=GREETING, reply_markup=start_keyboard)


@router.callback_query(F.data == MainMenuButtons.INSTRUCTIONS.value[1])
async def support(callback: CallbackQuery):
    """Instructions button handler."""
    await callback.message.answer(
        text=InstructionAnswers.TEXT
    )
    await callback.message.answer_document(
        document=InstructionAnswers.CHECK_LIST_PDF
    )
    await callback.message.answer_video(
        video=InstructionAnswers.VIDEO_INSTRUCTION_MOV
    )
    await callback.answer()


# # Обработчик всех типов сообщений
# @router.message()
# async def handle_docs(message: Message):
#     document = message.video
#     file_id = document.file_id
#     await message.reply(f"File ID: {file_id}")
