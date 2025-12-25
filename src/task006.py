# 006
# Crie um programa que leia um número e mostre o seu dobro, o triplo e a raiz
# quadrada.

from math import sqrt

from cli.io import printf
from cli.io import inputf_int


if __name__ == "__main__":
    num = inputf_int("Digite um número inteiro: ")

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
