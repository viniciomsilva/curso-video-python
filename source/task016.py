# 016
# CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER E MOSTRE SUA PORÇÃO INTEIRA

from math import trunc

from utils import custom as cs


def run():
    num = float(input("Digite um número real qualquer: "))

    print(
        "A parte inteira do número digitado é: {}{}".format(
            cs.customize(style="bold", color="cyan"),
            trunc(num),
        )
    )


if __name__ == "__main__":
    run()
