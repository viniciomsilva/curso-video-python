# 002
# ESCREVA UM PROGRAMA QUE LEIA O DIA, O MÊS E O ANO DE NASCIMENTO DE UMA PESSOA
# E MOSTRE-OS

from scripts.custom import customize as cs


def run():
    dd = input("Dia = ")
    mm = input("Mês = ")
    yy = input("Ano = ")

    print(
        "Que bom! Você nasceu em: {}!".format(
            cs(f"{dd}/{mm}/{yy}", color="cyan"),
        )
    )
