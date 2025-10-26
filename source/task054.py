# 054
# Crie um programa que leia a data de nascimento de sete pessoas e mostre
# quantas já atingiram a maioridade e quantas ainda não.

from datetime import date


def run():
    adults = 0
    minors = 0
    this_year = date.today().year

    qnt = int(input("Quantidade de pessoas: "))

    for i in range(qnt):
        birth = int(input("Ano de nascimento da {}ª pessoa: ".format(i + 1)))
        if this_year - birth >= 21:
            adults += 1
        else:
            minors += 1

    print("\nExistem {} adultos e {} menores.".format(adults, minors))
