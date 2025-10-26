# 033
# Faça um programa que leia três números e mostre qual é o maior e qual o menor.

# 055
# Faça um programa que leia o peso de cinco pessoas e mostre o maior e o menor.

from cli.io import printf


def run():
    values = []
    qnt = int(input("Quantidade de valores: "))

    for i in range(qnt):
        number = float(input("Digite o {}º valor: ".format(i + 1)))
        values.append(number)

    printf(
        " {:<6.1f} é o maior ".format(max(values)),
        start="\n",
        style="bold",
        back="cyan",
    )
    printf(
        " {:<6.1f} é o menor ".format(min(values)),
        style="bold",
        back="magenta",
    )
