# 016
# Crie um programa que leia um número real qualquer e mostre sua porção inteira.

from math import trunc

from cli.io import inputf_flo
from cli.ux import customize


if __name__ == "__main__":
    num = inputf_flo("Digite um número real qualquer: ")

    print(
        "\nA parte inteira do número digitado é: {}".format(
            customize(
                trunc(num),
                style="bold",
                color="cyan",
            ),
        )
    )
