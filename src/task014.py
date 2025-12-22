# 014
# ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA EM ºC PARA ºF

from cli.io import printf


def fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def run():
    celsius = float(input("Digite a temperatura (ºC): "))

    printf(
        "{:.1f}ºC".format(celsius),
        start="\n",
        end="",
        style="bold",
        color="magenta",
    )
    print(" equivalem a ", end="")
    printf(
        "{:.1f}ºF".format(fahrenheit(celsius)),
        style="bold",
        color="cyan",
    )


if __name__ == "__main__":
    run()
