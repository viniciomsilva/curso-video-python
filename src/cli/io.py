from re import sub
from re import search

from classes.missing_input_error import MissingInputError
from scripts.custom import customize


EXIT_CMDS = ("n", "no", "exit")


def inputf(
    prompt: object = "",
    start: str = "",
    style: str = "",
    color: str = "",
) -> str:
    return input(customize(f"{start}{prompt}", style, color))


def inputf_int(
    prompt: object = "",
    start: str = "",
    style: str = "",
    color: str = "",
) -> int:
    while True:
        try:
            user = inputf(prompt, start, style, color).strip()

            if not user:
                raise MissingInputError()
            elif not user.isnumeric():
                raise Exception()

            return int(user)
        except (MissingInputError, KeyboardInterrupt):
            return 0
        except:
            printf("Valor inválido!", end=" ", color="magenta")


def inputf_flo(
    prompt: object = "",
    start: str = "",
    style: str = "",
    color: str = "",
) -> float:
    dot = 0

    while True:
        try:
            user = inputf(prompt, start, style, color).strip()

            if not user:
                raise MissingInputError()

            if search(r"[\s,]", user) or user.count(".") > 1:
                user = sub(r"[\s.,]+", "_", user)
                dot = user.rfind("_")
                user = user.replace("_", "")

            if dot >= len(user):
                user = f"{user}.0"
            elif dot > 0:
                user = f"{user[:dot]}.{user[dot:]}"

            return float(user)
        except (MissingInputError, KeyboardInterrupt):
            return 0
        except:
            printf("Valor inválido!", end=" ", color="magenta")


def printf(
    value: object = "",
    start: str = "",
    end: str = "\n",
    flush: bool = True,
    style: str = "",
    color: str = "",
    back: str = "",
) -> None:
    print(
        customize(f"{start}{value}", style, color, back),
        end=end,
        flush=flush,
    )
