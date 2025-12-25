# 018
# Faça um programa que leia o valor de um ângulo qualquer e mostre na tela os
# valores do seno, cosseno e tangente.

from math import cos
from math import radians
from math import sin
from math import tan

from cli.io import inputf_flo
from cli.io import printf


if __name__ == "__main__":
    angle = inputf_flo("Digite um ângulo: ")

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
