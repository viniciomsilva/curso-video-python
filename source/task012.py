# 012
# FAÇA UM PROGRAMA QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE-O COM 5% DE DESCONTO

from scripts.custom import customize


def calc_discount(price, discount):
    return price * (1 - discount / 100)


def run():
    price = float(input("Digite o valor do produto: R$ "))
    discount = float(input("Digite o desconto (%): "))

    print(
        customize(
            "\nValor total: R$ {:.2f}".format(
                calc_discount(price, discount),
            ),
            style="bold",
            color="cyan",
        )
    )
