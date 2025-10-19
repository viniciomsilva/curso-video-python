from time import sleep

from cli.io import printf


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
