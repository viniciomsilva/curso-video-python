# 051
# Desenvolva um programa que leia o primeiro termo e a razão de uma pa,
# mostrando os 10 primeiros termos dessa progressão.

# 061
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os
# 10 primeiros termos da progressão usando a estrutura WHILE.

# 062
# Melhore o DESAFIO 61, perguntando ao usuário se ele quer adicionar mais alguns
# termos. O programa encerra quando ele digitar que quer mais 0 termos.

from cli.io import inputf_int
from cli.io import leave
from cli.io import printf
from cli.ux import wait


def __calc(f: int, r: int, n: int) -> int:
    return f + (n - 1) * r


if __name__ == "__main__":
    ap: list[int] = []
    current = 1

    first = inputf_int("Primeiro termo: ")
    reason = inputf_int("Razão: ")

    while True:
        n = inputf_int("Quantos termos? ")

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

        if leave("Adicionar mais termos? [y/n]: "):
            break

        current = len(ap) + 1
