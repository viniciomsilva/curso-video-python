# 033
# FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL O MENOR.

from scripts.custom import customize


def run():
    numbers = []

    for i in range(3):
        number = int(input("Digite o {}º número: ".format(i + 1)))
        numbers.append(number)

    print(
        customize(
            " {:<4} é o maior ".format(max(numbers)),
            style="bold",
            back="cyan",
        )
    )
    print(
        customize(
            " {:<4} é o menor ".format(min(numbers)),
            style="bold",
            back="magenta",
        )
    )
