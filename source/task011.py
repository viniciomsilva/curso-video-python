# 011
# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que
# cada 1l de tinta pinta uma área de 2m²

# 096
# Faça um programa que tenha uma função chama área, que receba as dimensões dum
# tereno retangular (largura e comprimento) e mostre a área do terreno.

from cli.io import printf
from scripts.custom import customize


def __area(w: float, h: float):
    return w * h


def __ink(a, ink_a):
    return a / ink_a


def run():
    width = float(input("Largura (m): "))
    height = float(input("Altura ou Comprimento (m): "))

    area = __area(width, height)

    printf(
        "Você precisará de {} de tinta para pintar uma área de {}!".format(
            customize(
                f"{__ink(area, 2):.1f}L",
                style="under",
                color="cyan",
            ),
            customize(
                f"{area:.2f}m²",
                style="under",
                color="magenta",
            ),
        ),
        start="\n",
    )
