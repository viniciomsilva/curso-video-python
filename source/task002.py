# 002
# ESCREVA UM PROGRAMA QUE LEIA O DIA, O MÊS E O ANO DE NASCIMENTO DE UMA PESSOA
# E MOSTRE-OS

from scripts.custom import customize


def run():
    dd = input("Dia = ")
    mm = input("Mês = ")
    yy = input("Ano = ")

    print(
        "Que bom! Você nasceu em: {}!".format(
            customize(
                "{}/{}/{}".format(
                    dd,
                    mm,
                    yy,
                ),
                color="cyan",
            ),
        )
    )
