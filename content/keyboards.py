from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from content.buttons import (
    ButtonsEnum, EmployeeButtons, InstructionsButtons, MainMenuButtons,
    SupportButtons, TO_MAIN_MENU
)


def inline_keyboard_builder(buttons: ButtonsEnum) -> InlineKeyboardMarkup:
    """InlineKeyboard designer."""
    builder = InlineKeyboardBuilder()
    for button in buttons:
        text, data = button.value
        builder.add(InlineKeyboardButton(text=text, callback_data=data))
    builder.adjust(2)
    return builder.as_markup()


def url_keyboard_builder(buttons: ButtonsEnum) -> InlineKeyboardMarkup:
    """InlineKeyboard designer for url buttons."""
    builder = InlineKeyboardBuilder()
    for button in buttons:
        text, data = button.value
        builder.add(InlineKeyboardButton(text=text, url=data))
    builder.add(InlineKeyboardButton(
        text=TO_MAIN_MENU[0], callback_data=TO_MAIN_MENU[1])
    )
    builder.adjust(3, 2, 1)
    return builder.as_markup()


start_keyboard = inline_keyboard_builder(MainMenuButtons)
employee_keyboard = inline_keyboard_builder(EmployeeButtons)
instructions_keyboard = inline_keyboard_builder(InstructionsButtons)
support_keyboard = url_keyboard_builder(SupportButtons)
