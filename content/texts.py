from enum import Enum


GREETING = (
    "Welcome to our Team! 🙌\n"
    "Привет и добро пожаловать в нашу команду!\n\n"
    "Спасибо, что выбрали нашу компанию, чтобы делать мир чище и красивее. "
    "Я искренне надеюсь, что у нас сложится взаимовыгодная и долгосрочная "
    "работа."
)


class InstructionAnswers(str, Enum):
    """Answers for the instruction section."""

    TEXT = (
        "Для того чтобы наши клиенты всегда оставались довольны, ❗️важно❗️ "
        "придерживаться стандартов качества при выполнении уборки. "
        "В этом разделе вы найдете все необходимые материалы для обучения "
        "и повышения вашего профессионального уровня 🧐.\n\n"

        "Пожалуйста, внимательно изучите представленные инструкции и файлы. "
        "Они помогут вам выполнять свою работу максимально эффективно и "
        "качественно 😎.\n\n"
        "Если у вас возникнут вопросы или потребуется дополнительная "
        "информация, не стесняйтесь обращаться за помощью 🥰. \n"
        "Спасибо за ваш труд и стремление к совершенству!"
    )
    CHECK_LIST_PDF = (
        "BQACAgIAAxkBAAMzZqVZ3zKlMLtysjDIO8uz0VvQwxcAAo5HAAIsQjBJEWSSzMbV2iQ1BA" # noqa
    )
    VIDEO_INSTRUCTION_MOV = (
        "BAACAgIAAxkBAAM2ZqVay9meWDlkZg667iN1_eGaey8AApNHAAIsQjBJszXiJpoJt8s1BA" # noqa
    )


class EmployeeAnswers(str, Enum):
    """Answers for the employee section."""

    TEXT = "{}, привет! Выбери один из пунктов меню!"
