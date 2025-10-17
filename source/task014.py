# 014
# ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA EM ºC PARA ºF

from utils import custom as cs


def fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def run():
    celsius = float(input("DIGITE A TEMPERATURA EM ºC: "))

    print(
        "{} = {}".format(
            cs.colorize(f"{celsius:.1f}ºC", color="lilac"),
            cs.colorize(f"{fahrenheit(celsius):.1f}ºF", color="cyan"),
        )
    )


if __name__ == "__main__":
    run()
