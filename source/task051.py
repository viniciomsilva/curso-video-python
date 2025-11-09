# 051
# Desenvolva um programa que leia o primeiro termo e a razão de uma pa,
# mostrando os 10 primeiros termos dessa progressão.

# 061
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os
# 10 primeiros termos da progressão usando a estrutura WHILE.

# 062
# Melhore o DESAFIO 61, perguntando ao usuário se ele quer adicionar mais alguns
# termos. O programa encerra quando ele digitar que quer mais 0 termos.

from cli.io import EXIT_CMDS
from cli.io import printf
from cli.wait import wait


def __calc(f, r, n):
    return f + (n - 1) * r


def run():
    ap = []
    current = 1

    first = int(input("Primeiro termo: "))
    reason = int(input("Razão: "))

    while True:
        n = int(input("Quantos termos? "))

        for i in range(current, (current + n)):
            ap.append(__calc(first, reason, i))

        wait("Calculando...")
        printf(
            ", ".join(map(str, ap)),
            end=", ",
            style="bold",
        )
        printf(
            "Fim!",
            style="bold",
            color="cyan",
        )

        if input("Adicionar mais termos? [y/n]: ") in EXIT_CMDS:
            break

        current = len(ap) + 1
