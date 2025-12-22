# 018
# FAÇA UM PROGRAMA QUE LEIA O VALOR DE UM ÂNGULO QUALQUER E MOSTRE NA TELA OS
# VALORES DO SENO, COSSENO E TANGENTE

from math import cos
from math import radians
from math import sin
from math import tan

from cli.io import printf


def run():
    angle = float(input("Digite um ângulo: "))

    printf(
        " Sin({:.1f}º) = {:.6f} ".format(
            angle,
            sin(radians(angle)),
        ),
        start="\n",
        style="bold",
        back="cyan",
    )
    printf(
        " Cos({:.1f}º) = {:.6f} ".format(
            angle,
            cos(radians(angle)),
        ),
        style="bold",
        back="yellow",
    )
    printf(
        " Tan({:.1f}º) = {:.6f} ".format(
            angle,
            tan(radians(angle)),
        ),
        style="bold",
        back="magenta",
    )


if __name__ == "__main__":
    run()
