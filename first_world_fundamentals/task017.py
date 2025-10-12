# 017
# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DOS CATETOS OPOSTO E ADJACENTE
# DE UM TRIANGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

from math import hypot

from custom import customize


if __name__ == "__main__":
    a = float(input("DIGITE O VALOR DE A: "))
    b = float(input("DIGITE O VALOR DE B: "))

    print(
        "A HIPOTENUSA VALE..: {}{:.2f}".format(
            customize(style="bold", color="cyan"),
            hypot(a, b),
        )
    )
