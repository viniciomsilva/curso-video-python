# 002
# Escreva um programa que leia o dia, o mês e o ano de nascimento de uma pessoa
# e mostre-os.

from cli.io import printf


if __name__ == "__main__":
    dd = input("Digite o dia: ")
    mm = input("Digite o mês: ")
    yy = input("Agora, digite o ano: ")

    printf(
        "Que bom! Você nasceu em: {}/{}/{}!".format(dd, mm, yy),
        start="\n",
        style="bold",
        color="cyan",
    )
