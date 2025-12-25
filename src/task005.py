# 005
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e
# antecessor.

from cli.io import printf
from cli.io import inputf_int


if __name__ == "__main__":
    num = inputf_int("Digite um número inteiro qualquer: ")

    printf(
        " Antecessor: {:4} ".format(num - 1),
        start="\n",
        style="bold",
        back="cyan",
    )
    printf(
        " Sucessor..: {:4} ".format(num + 1),
        style="bold",
        back="magenta",
    )
