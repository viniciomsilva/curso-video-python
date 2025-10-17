# 018
# FAÇA UM PROGRAMA QUE LEIA O VALOR DE UM ÂNGULO QUALQUER E MOSTRE NA TELA OS
# VALORES DO SENO, COSSENO E TANGENTE

from math import cos
from math import radians
from math import sin
from math import tan

from utils import custom as cs


def run():
    angle = float(input("Digite um ângulo: "))

    print(
        cs.colorize(
            f" Sin({angle:.1f}º) = {sin(radians(angle)):.6f} ",
            back="cyan",
        )
    )
    print(
        cs.colorize(
            f" Cos({angle:.1f}º) = {cos(radians(angle)):.6f} ",
            back="lilac",
        )
    )
    print(
        cs.colorize(
            f" Tan({angle:.1f}º) = {tan(radians(angle)):.6f} ",
            back="yellow",
        )
    )


if __name__ == "__main__":
    run()
