from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery


async def delete_or_continue(callback: CallbackQuery) -> None:
    """
    Attempts to delete a message in response to a callback query.

    If the message is older than allowed by Telegram,
    the function silently continues without raising an exception.
    """
    try:
        await callback.message.delete()
    except TelegramBadRequest:
        return
