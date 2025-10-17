STYLES = {
    "bold": "1",
    "underline": "4",
    "negative": "7",
}

COLORS = {
    "white": ";30",
    "red": ";31",
    "green": ";32",
    "yellow": ";33",
    "blue": ";34",
    "lilac": ";35",
    "cyan": ";36",
    "gray": ";37",
}

BACKS = {
    "white": ";40m",
    "red": ";41m",
    "green": ";42m",
    "yellow": ";43m",
    "blue": ";44m",
    "lilac": ";45m",
    "cyan": ";46m",
    "gray": ";47m",
}


def clean():
    return "\033[m"


def customize(style="", color="", back="") -> str:
    cod = "\033["

    cod += STYLES[style] if (style != "") else ""
    cod += COLORS[color] if (color != "") else ""
    cod += BACKS[back] if (back != "") else "m"

    return cod


def bold(text):
    return f"{customize("bold")}{text}{clean()}"


def colorize(text, color="", back=""):
    return f"{customize("bold", color, back)}{text}{clean()}"

# TODO Desenvolver função printf
