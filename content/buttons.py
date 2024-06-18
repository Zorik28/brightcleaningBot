from enum import Enum


class MainButtons(Enum):
    """Unified enum for main menu button text and callback data."""

    ADMIN = ("👮‍♀️ADMINISTRATION", 'admin')
    EMPLOYEE = ("👩‍🏭EMPLOYEE", 'employee')
    INSTRUCTIONS = ("📝INSTRUCTIONS", 'instructions')
    SUPPORT = ("🆘SUPPORT", 'support')
