# 005
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E
# ANTECESSOR

from scripts.custom import customize


def run():
    num = int(input("Digite um número inteiro qualquer: "))

    print(
        customize(
            " Antecessor: {:4} ".format(num - 1),
            style="bold",
            back="cyan",
        )
    )
    print(
        customize(
            " Sucessor..: {:4} ".format(num + 1),
            style="bold",
            back="magenta",
        )
    )
