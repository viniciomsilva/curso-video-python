# 079
# Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os numa lista. Caso o valor digitado já exista, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

from cli.io import inputf_int
from cli.io import leave
from cli.io import printf
from cli.ux import wait


if __name__ == "__main__":
    values: list[int] = []

    while True:
        v = inputf_int("Digite um valor: ")

        if not v in values:
            values.append(v)

        if leave("Quer continuar? [y/n] "):
            break

    wait("Analisando...")
    printf(
        "Você digitou os valores: {}".format(
            sorted(values),
        ),
        style="bold",
        color="cyan",
    )
