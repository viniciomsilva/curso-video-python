# 033
# Faça um programa que leia três números e mostre qual é o maior e qual o menor.

# 055
# Faça um programa que leia o peso de cinco pessoas e mostre o maior e o menor.

# 078
# Faça um programa que leia 5 valores numéricos e guarde-os numa lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

# 099
# Faça um programa que tenha uma função chamada maior, que receba vários
# parâmetros com valores inteiros. Seu programa tem que analisar todos os
# valores e dizer qual deles é o maior.

from random import randint

from cli.io import inputf_int
from cli.io import printf


if __name__ == "__main__":
    mn = 0
    mx = 0
    pos_mn: list[int] = []
    pos_mx: list[int] = []
    values: list[int] = []

    printf("Digite -1 para gerar aleatoriamente...", color="yellow")
    qnt = inputf_int("Quantidade de valores: ")

    if qnt <= 0:
        values = [randint(1, 100) for _ in range(5)]
        printf("Valores sorteados: {}.".format(", ".join(map(str, values))))
    else:
        for i in range(qnt):
            num = inputf_int(f"Digite o {(i + 1)}º valor: ")
            values.append(num)

    mn = min(values)
    mx = max(values)

    for i, v in enumerate(values):
        if v == mn:
            pos_mn.append(i)
        if v == mx:
            pos_mx.append(i)

    printf(
        " Maior: ({:^3}) ~> Posição(ões): ({}) ".format(
            mx,
            ", ".join(map(str, pos_mx)),
        ),
        start="\n",
        style="bold",
        back="cyan",
    )
    printf(
        " Maior: ({:^3}) ~> Posição(ões): ({}) ".format(
            mn,
            ", ".join(map(str, pos_mn)),
        ),
        style="bold",
        back="magenta",
    )
