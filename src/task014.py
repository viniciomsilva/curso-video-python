# 014
# Escreva um programa que converta uma temperatura em ºC para ºF.

from cli.io import inputf_flo
from cli.io import printf


def __fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    celsius = inputf_flo("Digite a temperatura (ºC): ")

    printf(
        "{:.1f}ºC".format(celsius),
        start="\n",
        end="",
        style="bold",
        color="magenta",
    )
    print(" equivalem a ", end="")
    printf(
        "{:.1f}ºF".format(__fahrenheit(celsius)),
        style="bold",
        color="cyan",
    )
