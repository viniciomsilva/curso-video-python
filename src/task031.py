# 031
# Desenvolva um programa que pergunte a distância de uma viagem em km. calcule o
# preço da passagem, cobrando R$ 0,50/km para viagens de até 200km e R$ 0,45/km
# para viagens mais distantes.

from cli.io import inputf_flo
from cli.io import printf
from cli.ux import brl


def __calc(distance: float) -> float:
    return distance * 0.45 if distance > 200 else distance * 0.5


if __name__ == "__main__":
    distance = inputf_flo("Digite a distância da viagem (km): ")

    printf(
        "O valor da passagem é {}".format(brl(__calc(distance))),
        start="\n",
        style="bold",
        color="cyan",
    )
