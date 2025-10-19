# 031
# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM. CALCULE O
# PREÇO DA PASSAGEM, COBRANDO R$ 0,50 POR KM PARA VIAGENS DE ATÉ 200KM E R$ 0,45
# POR KM PARA VIAGENS MAIS DISTANTES.

from cli.io import printf


def __calc(distance):
    return distance * 0.45 if distance > 200 else distance * 0.5


def run():
    distance = float(input("Digite a distância da viagem (km): "))

    printf(
        "O valor da passagem é R${:.2f}".format(__calc(distance)),
        start="\n",
        style="bold",
        color="cyan",
    )
