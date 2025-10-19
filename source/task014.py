# 014
# ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA EM ºC PARA ºF

from scripts.custom import customize


def fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def run():
    celsius = float(input("Digite a temperatura (ºC): "))

    print(
        "{} = {}".format(
            customize(
                "{:.1f}ºC".format(celsius),
                color="magenta",
            ),
            customize(
                "{:.1f}ºF".format(fahrenheit(celsius)),
                color="cyan",
            ),
        )
    )
