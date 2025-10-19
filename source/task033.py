# 033
# FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL O MENOR.

from cli.io import printf


def run():
    numbers = []

    for i in range(3):
        number = int(input("Digite o {}º número: ".format(i + 1)))
        numbers.append(number)

    printf(
        " {:<4} é o maior ".format(max(numbers)),
        start="\n",
        style="bold",
        back="cyan",
    )
    printf(
        " {:<4} é o menor ".format(min(numbers)),
        style="bold",
        back="magenta",
    )
