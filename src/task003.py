# 003
# FAÇA UM PROGRAMA QUE LEIA DOIS NÚMEROS E MOSTRE A SOMA ENTRE ELES

from cli.io import printf


def run():
    num1 = float(input("Digite o 1º número: "))
    num2 = float(input("Digite o 2º número: "))

    printf(
        "A soma é igual a: {}".format(num1 + num2),
        start="\n",
        style="bold",
        color="cyan",
    )


if __name__ == "__main__":
    run()
