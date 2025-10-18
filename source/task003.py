# 003
# FAÇA UM PROGRAMA QUE LEIA DOIS NÚMEROS E MOSTRE A SOMA ENTRE ELES

from scripts.custom import customize as cs


def run():
    num1 = float(input("Digite o 1º número: "))
    num2 = float(input("Digite o 2º número: "))

    print(
        "A soma é igual a: {}".format(
            cs((num1 + num2), "bold", "cyan"),
        )
    )
