# 006
# CRIE UM PROGRAMA QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, O TRIPLO E A RAIZ
# QUADRADA

from math import sqrt

from scripts.custom import customize


def run():
    num = int(input("Digite um número inteiro: "))

    print(
        customize(
            " Dobro........: {:8} ".format(
                num * 2,
            ),
            style="bold",
            back="cyan",
        )
    )
    print(
        customize(
            " Triplo.......: {:8} ".format(
                num * 3,
            ),
            style="bold",
            back="magenta",
        )
    )
    print(
        customize(
            " Raiz Quadrada: {:8} ".format(
                sqrt(num),
            ),
            style="bold",
            back="yellow",
        )
    )
