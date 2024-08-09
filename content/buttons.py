from enum import Enum


class ButtonsEnum(Enum):
    """Parent class for all enum buttons."""


class MainMenuButtons(ButtonsEnum):
    """Unified enum for main menu button text and callback data."""

    ADMIN = ("👮‍♀️ADMINISTRATION", 'admin')
    EMPLOYEE = ("👩‍🏭EMPLOYEE", 'employee')
    INSTRUCTIONS = ("📝INSTRUCTIONS", 'instructions')
    SUPPORT = ("🆘SUPPORT", 'support')


class EmployeeButtons(ButtonsEnum):
    """Unified enum for employee button text and callback data."""

    UPLOAD_ID = ("Upload ID 🪪", 'upload_id')
    WEEKLY_SCHEDULE = ("Weekly Schedule 📅", 'schedule')
    UPLOAD_EXPENSES = ("Upload Expenses 🫰", 'expenses')
    SEE_MY_PROGRESS = ("See my progress 📊", 'progress')
    TO_MAIN_MENU = ("⬅️to Main Menu", 'return')


class SupportButtons(ButtonsEnum):
    """Unified enum for support button text and url."""

    TANYA = ("Татьяна👧🏻", 'https://t.me/+380982522681')
    RAMELA = ("Рамела👩🏻", 'https://t.me/ramelaruti')
    EKATERINA = ("Екатерина👩🏼", 'https://t.me/KathrynK0')
    INSTAGRAM = ("Instagram📷", 'instagram.com/brightcleaningnyc')
    WEB_SITE = ("Our Web Site🌐", 'brightcleaningnyc.com')


class InstructionsButtons(ButtonsEnum):
    """Unified enum for instructions button text and callback data."""

    FILE = ("Cleaning Check List", 'file')
    VIDEO = ("Video Instruction", 'video')
    TO_MAIN_MENU = ("⬅️to Main Menu", 'return')


TO_MAIN_MENU = ("⬅️to Main Menu", 'return')
