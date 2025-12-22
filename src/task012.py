# 012
# FAÇA UM PROGRAMA QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE-O COM 5% DE DESCONTO

from cli.io import printf


def __calc(price, discount):
    return price * (1 - discount / 100)


def run():
    price = float(input("Digite o valor do produto: R$ "))
    discount = float(input("Digite o desconto (%): "))

    printf(
        "Valor total: R$ {:.2f}".format(__calc(price, discount)),
        start="\n",
        style="bold",
        color="cyan",
    )


if __name__ == "__main__":
    run()
