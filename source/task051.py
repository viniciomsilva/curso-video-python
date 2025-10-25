# 051
# Desenvolva um programa que leia o primeiro termo e a razão de uma pa,
# mostrando os 10 primeiros termos dessa progressão.

from cli.io import printf


def __calc(a, r, n):
    return a + (n - 1) * r


def run():
    a = int(input("Primeiro termo: "))
    r = int(input("Razão: "))
    n = int(input("Quantos termos? "))

    print()
    for i in range(1, (n + 1)):
        printf(
            __calc(a, r, i),
            end=", ",
            style="bold",
        )

    printf(
        "Fim!",
        style="bold",
        color="cyan",
    )
