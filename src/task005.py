# 005
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E
# ANTECESSOR

from cli.io import printf


def run():
    num = int(input("Digite um número inteiro qualquer: "))

    printf(
        " Antecessor: {:4} ".format(num - 1),
        start="\n",
        style="bold",
        back="cyan",
    )
    printf(
        " Sucessor..: {:4} ".format(num + 1),
        style="bold",
        back="magenta",
    )


if __name__ == "__main__":
    run()
