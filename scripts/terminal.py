import os


COMMAND_CLEAR = "clear" if os.name != "nt" else "cls"


def clear():
    os.system(COMMAND_CLEAR)
