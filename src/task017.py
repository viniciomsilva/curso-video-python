# 017
# Faça um programa que leia o comprimento dos catetos oposto e adjacente
# de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

from cli.io import inputf_flo
from cli.io import printf


if __name__ == "__main__":
    a = inputf_flo("Digite o valor de A: ")
    b = inputf_flo("Digite o valor de B: ")

    printf(
        "A hipotenusa vale: {:.2f}".format(hypot(a, b)),
        start="\n",
        style="under",
        color="cyan",
    )
