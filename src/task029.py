# 029
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 para cada km acima do limite.

from cli.io import inputf_flo
from cli.io import printf
from cli.ux import brl


def __calc(speed: float) -> float:
    return (speed - 80) * 7


if __name__ == "__main__":
    speed = inputf_flo("Digite a velocidade do carro (km/h): ")

    if speed <= 80:
        printf(
            "Tudo bem!",
            style="bold",
            color="cyan",
        )
    else:
        printf(
            "Você foi multado em {}!".format(brl(__calc(speed))),
            style="bold",
            color="magenta",
        )
