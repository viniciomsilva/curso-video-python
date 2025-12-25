import os
from datetime import datetime as dt
from time import sleep

from cli.io import printf


__CMD_CLEAR = "clear" if os.name != "nt" else "cls"


__STYLES = {
    "bold": "1",
    "under": "4",
    "invert": "7",
    "through": "9",
}

__COLORS = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37",
}

__BACKS = {
    "black": "40",
    "red": "41",
    "green": "42",
    "yellow": "43",
    "blue": "44",
    "magenta": "45",
    "cyan": "46",
    "white": "47",
}

THIS_YEAR = dt.today().year


def __clear() -> str:
    return "\033[0m"


def __code(
    style: str,
    color: str,
    back: str,
) -> str:
    cod = "\033["

    cod += "" if not style else f"{__STYLES[style]}"
    cod += "" if not color else f";{__COLORS[color]}"
    cod += "m" if not back else f";{__BACKS[back]}m"

    return cod


def brl(value: object, sing: str = "R$") -> str:
    r = f"{sing} {value:,.2f}"
    return r.replace(",", "_").replace(".", ",").replace("_", ".")


def clear():
    os.system(__CMD_CLEAR)


def customize(
    value: object,
    style: str = "",
    color: str = "",
    back: str = "",
) -> str:
    return "{}{}{}".format(
        __code(style, color, back),
        value,
        __clear(),
    )


def wait(
    msg: object,
    time: int = 2,
    end: str = "\n\n",
    style: str = "bold",
    color: str = "green",
) -> None:
    printf(
        msg,
        start="\n",
        end=end,
        style=style,
        color=color,
    )
    sleep(time)
