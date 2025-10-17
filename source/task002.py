# 002
# ESCREVA UM PROGRAMA QUE LEIA O DIA, O MÊS E O ANO DE NASCIMENTO DE UMA PESSOA
# E MOSTRE-OS

from utils import custom as cs


def run():
    dd = input("Dia = ")
    mm = input("Mês = ")
    yy = input("Ano = ")

    print(
        "Que bom! Você nasceu em: {}{}/{}/{}{}!".format(
            cs.customize(style="bold", color="cyan"),
            dd,
            mm,
            yy,
            cs.clean(),
        )
    )


if __name__ == "__main__":
    run()
