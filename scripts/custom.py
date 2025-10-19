STYLES = {
    "bold": "1",
    "under": "4",
    "invert": "7",
    "through": "9",
}

COLORS = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37",
}

BACKS = {
    "black": "40",
    "red": "41",
    "green": "42",
    "yellow": "43",
    "blue": "44",
    "magenta": "45",
    "cyan": "46",
    "white": "47",
}


def __clear() -> str:
    return "\033[0m"


def __code(
    style: str,
    color: str,
    back: str,
) -> str:
    cod = "\033["

    cod += "" if not style else f"{STYLES[style]}"
    cod += "" if not color else f";{COLORS[color]}"
    cod += "m" if not back else f";{BACKS[back]}m"

    return cod


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
