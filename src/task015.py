# 015
# Escreva um programa que pergunte a quantidade de km percorridos por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
# pagar, sabendo que o carro custa R$ 60,00/dia e R$ 0,15/km rodado.

from cli.io import inputf_flo
from cli.io import inputf_int
from cli.io import printf
from cli.ux import brl


def __calc(days: int, kms: float) -> float:
    return days * 60 + kms * 0.15


if __name__ == "__main__":
    days = inputf_int("Digite a quantidade de dias: ")
    kms = inputf_flo("Digite quantos quilômetros foram rodados: ")

    printf(
        "Valor total: {}".format(brl(__calc(days, kms))),
        start="\n",
        style="bold",
        color="cyan",
    )
