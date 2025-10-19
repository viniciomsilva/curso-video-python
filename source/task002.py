# 002
# ESCREVA UM PROGRAMA QUE LEIA O DIA, O MÊS E O ANO DE NASCIMENTO DE UMA PESSOA
# E MOSTRE-OS

from cli.io import printf


def run():
    dd = input("Digite o dia: ")
    mm = input("Digite o mês: ")
    yy = input("Agora, digite o ano: ")

    printf(
        "Que bom! Você nasceu em: {}/{}/{}!".format(dd, mm, yy),
        start="\n",
        style="bold",
        color="cyan",
    )
