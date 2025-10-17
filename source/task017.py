# 017
# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DOS CATETOS OPOSTO E ADJACENTE
# DE UM TRIANGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

from math import hypot

from utils import custom as cs


def run():
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))

    print(
        "A hipotenusa vale: {}".format(
            cs.colorize(f"{hypot(a, b):.2f}", color="cyan"),
        )
    )


if __name__ == "__main__":
    run()
