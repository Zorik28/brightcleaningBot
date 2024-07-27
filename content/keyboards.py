from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from content.buttons import (
    ButtonsEnum, EmployeeButtons, InstructionsButtons, MainMenuButtons
)


def inline_keyboard_builder(
    buttons: ButtonsEnum | None = None,
    exclude: ButtonsEnum | None = None,
    only: ButtonsEnum | None = None
) -> InlineKeyboardMarkup:
    """
    InlineKeyboard designer.

    If `exclude_button` is passed, the button is removed.

    If `only` is passed, the keyboard will only contain one button.
    """
    builder = InlineKeyboardBuilder()
    if only:
        text, data = only.value
        builder.add(InlineKeyboardButton(text=text, callback_data=data))
        return builder.as_markup()
    for button in buttons:
        if button != exclude:
            text, data = button.value
            builder.add(InlineKeyboardButton(text=text, callback_data=data))
    builder.adjust(2)
    return builder.as_markup()


start_keyboard = inline_keyboard_builder(MainMenuButtons)
instructions_keyboard = inline_keyboard_builder(InstructionsButtons)
employee_keyboard = inline_keyboard_builder(EmployeeButtons)
