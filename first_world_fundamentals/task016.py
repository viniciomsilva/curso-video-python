# 016
# CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER E MOSTRE SUA PORÇÃO INTEIRA

from math import trunc

from custom import customize


if __name__ == "__main__":
    num = float(input("DIGITE UM NÚMERO REAL QUALQUER......: "))

    print(
        "A PARTE INTEIRA DO NÚMERO DIGITADO É: {}{}".format(
            customize(style="bold", color="cyan"),
            trunc(num),
        )
    )
