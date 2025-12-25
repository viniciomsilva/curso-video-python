# 003
# Faça um programa que leia dois números e mostre a soma entre eles.

from cli.io import printf
from cli.io import inputf_flo


if __name__ == "__main__":
    num1 = inputf_flo("Digite o 1º número: ")
    num2 = inputf_flo("Digite o 2º número: ")

    printf(
        "A soma é igual a: {}".format(num1 + num2),
        start="\n",
        style="bold",
        color="cyan",
    )
