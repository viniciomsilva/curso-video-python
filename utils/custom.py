styles = {"bold": "1", "underline": "4", "negative": "7"}

colors = {
    "white": ";30",
    "red": ";31",
    "green": ";32",
    "yellow": ";33",
    "blue": ";34",
    "lilac": ";35",
    "cyan": ";36",
    "gray": ";37",
}

backs = {
    "white": ";40m",
    "red": ";41m",
    "green": ";42m",
    "yellow": ";43m",
    "blue": ";44m",
    "lilac": ";45m",
    "cyan": ";46m",
    "gray": ";47m",
}


def clear():
    return "\033[m"


def customize(style="", color="", back="") -> str:
    cod = "\033["

    cod += styles[style] if style != "" else ""
    cod += colors[color] if color != "" else ""
    cod += backs[back] if back != "" else "m"

    return cod
