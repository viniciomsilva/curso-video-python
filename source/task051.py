# 051
# Desenvolva um programa que leia o primeiro termo e a razão de uma pa,
# mostrando os 10 primeiros termos dessa progressão.

# 061
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os
# 10 primeiros termos da progressão usando a estrutura WHILE.

from cli.io import printf
from cli.wait import wait


def __calc(a, r, n):
    return a + (n - 1) * r


def run():
    ap = []
    a = int(input("Primeiro termo: "))
    r = int(input("Razão: "))
    n = int(input("Quantos termos? "))

    for i in range(1, (n + 1)):
        ap.append(__calc(a, r, i))

    wait("Calculando...")
    printf(
        ", ".join(map(str, ap)),
        end=" ",
        style="bold",
    )
    printf(
        "Fim!",
        style="bold",
        color="cyan",
    )
