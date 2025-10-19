# 018
# FAÇA UM PROGRAMA QUE LEIA O VALOR DE UM ÂNGULO QUALQUER E MOSTRE NA TELA OS
# VALORES DO SENO, COSSENO E TANGENTE

from math import cos
from math import radians
from math import sin
from math import tan

from scripts.custom import customize


def run():
    angle = float(input("Digite um ângulo: "))

    print(
        customize(
            "\n Sin({:.1f}º) = {:.6f} ".format(
                angle,
                sin(radians(angle)),
            ),
            back="cyan",
        )
    )
    print(
        customize(
            " Cos({:.1f}º) = {:.6f} ".format(
                angle,
                cos(radians(angle)),
            ),
            back="yellow",
        )
    )
    print(
        customize(
            " Tan({:.1f}º) = {:.6f} ".format(
                angle,
                tan(radians(angle)),
            ),
            back="magenta",
        )
    )
