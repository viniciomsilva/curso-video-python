# 033
# Faça um programa que leia três números e mostre qual é o maior e qual o menor.

# 055
# Faça um programa que leia o peso de cinco pessoas e mostre o maior e o menor.

from random import randint

from cli.io import printf


def run():
    values = []

    printf("Digite -1 para gerar aleatoriamente...", color="yellow")
    qnt = int(input("Quantidade de valores: "))

    if qnt <= 0:
        values = [randint(1, 100) for _ in range(5)]
        printf("Valores sorteados: {}".format(values))
    else:
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
