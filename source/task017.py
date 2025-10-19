# 017
# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DOS CATETOS OPOSTO E ADJACENTE
# DE UM TRIANGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

from math import hypot

from scripts.custom import customize


def run():
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))

    print(
        "A hipotenusa vale: {}".format(
            customize(
                "{:.2f}".format(hypot(a, b)),
                style="under",
                color="cyan",
            ),
        )
    )
