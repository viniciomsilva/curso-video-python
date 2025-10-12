# 002
# ESCREVA UM PROGRAMA QUE LEIA O DIA, O MÊS E O ANO DE NASCIMENTO DE UMA PESSOA
# E MOSTRE-OS

from custom import clear
from custom import customize

if __name__ == "__main__":
    dd = input("DIA = ")
    mm = input("MÊS = ")
    yy = input("ANO = ")

    print(
        "QUE BOM, VOCÊ NASCEU EM {}{}/{}/{}{}!".format(
            customize(style="bold", color="cyan"),
            dd,
            mm,
            yy,
            clear(),
        )
    )
