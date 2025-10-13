from sys import path as syspath
from os import path as path

syspath.append(path.abspath(path.join(path.dirname(__file__), "..")))

from utils import clear
from utils import customize


def bold(text):
    return f"{customize("bold")}{text}{clear()}"


def colorize(text, color="", back=""):
    return f"{customize("bold", color, back)}{text}{clear()}"
