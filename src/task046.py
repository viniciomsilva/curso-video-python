# 046
# Faça um programa que mostre a contagem regressiva para a queima de fogos de
# artifício, indo de 10 a 0 com pausa de 1 segundo.

from time import sleep

from cli.io import inputf_int
from cli.io import printf


if __name__ == "__main__":
    seconds = inputf_int("Quantidade de segundos: ")

    if seconds <= 0 or seconds > 30:
        seconds = 30

    for i in range(seconds, 0, -1):
        print(
            f"{i}{" " * 4}",
            end="\r",
        )
        sleep(1)

    printf(
        "🎉 🎉 🎉",
        start="\n",
    )
