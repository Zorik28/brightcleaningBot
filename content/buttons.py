from enum import Enum


class ButtonsEnum(Enum):
    """Main class for"""
    pass


class MainMenuButtons(ButtonsEnum):
    """Unified enum for main menu button text and callback data."""

    ADMIN = ("👮‍♀️ADMINISTRATION", 'admin')
    EMPLOYEE = ("👩‍🏭EMPLOYEE", 'employee')
    INSTRUCTIONS = ("📝INSTRUCTIONS", 'instructions')
    SUPPORT = ("🆘SUPPORT", 'support')
