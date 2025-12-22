# 016
# CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER E MOSTRE SUA PORÇÃO INTEIRA

from math import trunc

from scripts.custom import customize


def run():
    num = float(input("Digite um número real qualquer: "))

    print(
        "\nA parte inteira do número digitado é: {}".format(
            customize(
                trunc(num),
                style="bold",
                color="cyan",
            ),
        )
    )


if __name__ == "__main__":
    run()
