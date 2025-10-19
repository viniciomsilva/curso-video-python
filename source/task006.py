# 006
# CRIE UM PROGRAMA QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, O TRIPLO E A RAIZ
# QUADRADA

from math import sqrt

from cli.io import printf


def run():
    num = int(input("Digite um número inteiro: "))

    printf(
        " Dobro........: {:8} ".format(num * 2),
        start="\n",
        style="bold",
        back="cyan",
    )
    printf(
        " Triplo.......: {:8} ".format(num * 3),
        style="bold",
        back="magenta",
    )
    printf(
        " Raiz Quadrada: {:8} ".format(sqrt(num)),
        style="bold",
        back="yellow",
    )
