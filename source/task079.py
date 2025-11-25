# 079
# Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os numa lista. Caso o valor digitado já exista, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

from cli.io import EXIT_CMDS
from cli.io import printf
from cli.wait import wait


def run():
    values = []

    while True:
        v = input("Digite um valor: ")

        if not v.isnumeric():
            print("Por favor! ", end="")
            continue
        elif not v in values:
            values.append(v)

        if input("Quer continuar? [S/N] ").strip().lower() in EXIT_CMDS:
            break

    wait("Analisando...")
    printf(
        "Você digitou os valores: {}".format(
            sorted(map(int, values)),
        ),
        style="bold",
        color="cyan",
    )
