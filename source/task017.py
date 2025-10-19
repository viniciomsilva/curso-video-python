# 017
# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DOS CATETOS OPOSTO E ADJACENTE
# DE UM TRIANGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

from math import hypot

from cli.io import printf


def run():
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))

    printf(
        "A hipotenusa vale: {:.2f}".format(hypot(a, b)),
        start="\n",
        style="under",
        color="cyan",
    )
