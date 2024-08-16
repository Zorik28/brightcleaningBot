# flake8: noqa: E501

from enum import Enum

GREETING = (
    "Welcome to our Team! 🙌\n"
    "Привет и добро пожаловать в нашу команду!\n\n"
    "Спасибо, что выбрали нашу компанию, чтобы делать мир чище и красивее. "
    "Я искренне надеюсь, что у нас сложится взаимовыгодная и долгосрочная "
    "работа."
)

SUPPORT = "По контактам ниже вы сможете с нами связаться."

class InstructionAnswers(Enum):
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
    AIRBNB_PHOTOS_1 = (
        'AgACAgIAAxkBAAIB0ma_sYkwQGl2lhXtgz4RqMY6yEcVAALA4DEbeJ8AAUqxr7DLdQdCmQEAAwIAA3kAAzUE',
        'AgACAgIAAxkBAAIB1Ga_sbcTCdRYWbnP4VnwnuEorpECAAKx4DEbeJ8AAUr8MfdkTfxX6gEAAwIAA3kAAzUE',
        'AgACAgIAAxkBAAIB8Ga_tVHKphQuRKMAAe6iyrtl-yznVgACs-AxG3ifAAFKGUR4LHgm3LQBAAMCAAN5AAM1BA',
        'AgACAgIAAxkBAAIB8Wa_tVFGspuwXqs2e9GzrYNNJkiPAAK04DEbeJ8AAUqVvc8lpioPwAEAAwIAA3kAAzUE',
        'AgACAgIAAxkBAAIB82a_tVLrYGltv8t9HrUoWZVMHIIJAAK14DEbeJ8AAUrFlj1-EsJ5CgEAAwIAA3kAAzUE',
        'AgACAgIAAxkBAAIB9ma_tVLVQwmaDlA0lCDR-ofJzim9AAK24DEbeJ8AAUrs2vphSBsi-QEAAwIAA3kAAzUE',
        'AgACAgIAAxkBAAIB-Ga_tVJm1DiLCinYvQuiuyQWhxp-AAK34DEbeJ8AAUph7niiZLp9YwEAAwIAA3kAAzUE',
        'AgACAgIAAxkBAAIB-ma_tVIYQUxeMTi2uYO3j_LXcHA7AAK44DEbeJ8AAUpc8QbntTDPbgEAAwIAA3kAAzUE'
    )
    AIRBNB_PHOTOS_2 = (
        'AgACAgIAAxkBAAICCWa_tkaEAT1RnMlG1FsPMm_V2LbYAAKy4DEbeJ8AAUrCY7A1eD4JcAEAAwIAA3kAAzUE',
        'AgACAgIAAxkBAAICCma_tkbTcd21PX-JWn5ghUY6C60jAAK64DEbeJ8AAUpj05RULi8nRQEAAwIAA3kAAzUE',
        'AgACAgIAAxkBAAICC2a_tkavdcnfQiGxD_xOVZg2BFIFAAK54DEbeJ8AAUrG7KGQqAfTGgEAAwIAA3kAAzUE',
        'AgACAgIAAxkBAAICDGa_tkYvSooccE770-vmvv3xwVaHAAK74DEbeJ8AAUowWK1prEI7tQEAAwIAA3kAAzUE',
        'AgACAgIAAxkBAAICDma_tkZpbkSpK131O54LBDJzu_40AAK84DEbeJ8AAUp22b6Fx_6u2gEAAwIAA3kAAzUE',
        'AgACAgIAAxkBAAICE2a_tkYcGFCGqApON72XNfHf0cl1AAK94DEbeJ8AAUp4wt_Lw-6UVwEAAwIAA3kAAzUE',
        'AgACAgIAAxkBAAICFGa_tkaP8mpf-PGWh6LENpsU0mSMAAK-4DEbeJ8AAUotriLsbUF3AAEBAAMCAAN5AAM1BA',
        'AgACAgIAAxkBAAICFma_tkYCDljgvI4rBHdVZXM1QGRqAAK_4DEbeJ8AAUpEzM576KMQ8QEAAwIAA3kAAzUE'
    )
    CHECK_LIST_PDF = (
        "BQACAgIAAxkBAAMzZqVZ3zKlMLtysjDIO8uz0VvQwxcAAo5HAAIsQjBJEWSSzMbV2iQ1BA"
    )
    VIDEO_INSTRUCTION_MOV = (
        "BAACAgIAAxkBAAM2ZqVay9meWDlkZg667iN1_eGaey8AApNHAAIsQjBJszXiJpoJt8s1BA"
    )


class EmployeeAnswers(str, Enum):
    """Answers for the employee section."""

    TEXT = "{}, привет!\nВыбери один из пунктов:"
