# 012
# FAÇA UM PROGRAMA QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE-O COM 5% DE DESCONTO

from utils import custom as cs


def calc_discount(price, discount):
    return price * (1 - discount / 100)


def run():
    price = float(input("Digite o valor do produto...........: R$ "))
    discount = float(input("Digite a porcentagem de desconto (%):    "))

    print(
        cs.colorize(
            f"\nValor total: R$ {calc_discount(price, discount):.2f}",
            color="cyan",
        )
    )


if __name__ == "__main__":
    run()
