# 012
# Faça um programa que leia o preço de um produto e mostre-o com 5% de desconto.

from cli.io import inputf_flo
from cli.io import printf
from cli.ux import brl


def __calc(price: float, discount: float) -> float:
    return price * (1 - discount / 100)


if __name__ == "__main__":
    price = inputf_flo("Digite o valor do produto: R$ ")
    discount = inputf_flo("Digite o desconto (%): ")

    printf(
        "Valor total: {}".format(brl(__calc(price, discount))),
        start="\n",
        style="bold",
        color="cyan",
    )
