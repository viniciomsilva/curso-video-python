from scripts.custom import customize


def inputf(
    prompt: object = "",
    style: str = "",
    color: str = "",
) -> str:
    return input(customize(prompt, style, color))


def printf(
    value: object,
    start: str = "",
    end: str = "\n",
    style: str = "",
    color: str = "",
    back: str = "",
) -> None:
    print(
        customize(f"{start}{value}", style, color, back),
        end=end,
    )
