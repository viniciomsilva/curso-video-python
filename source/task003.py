# 003
# FAÇA UM PROGRAMA QUE LEIA DOIS NÚMEROS E MOSTRE A SOMA ENTRE ELES

from scripts.custom import customize


def run():
    num1 = float(input("Digite o 1º número: "))
    num2 = float(input("Digite o 2º número: "))

    print(
        "A soma é igual a: {}".format(
            customize(
                num1 + num2,
                style="bold",
                color="cyan",
            ),
        )
    )
