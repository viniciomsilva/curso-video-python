# 054
# Crie um programa que leia a data de nascimento de sete pessoas e mostre
# quantas já atingiram a maioridade e quantas ainda não.

from cli.io import inputf_int
from cli.ux import THIS_YEAR


if __name__ == "__main__":
    adults = 0
    minors = 0


    qnt = inputf_int("Quantidade de pessoas: ")

    for i in range(qnt):
        birth = inputf_int(f"Ano de nascimento da {(i + 1)}ª pessoa: ")
        if THIS_YEAR - birth >= 21:
            adults += 1
        else:
            minors += 1

    print(f"\nExistem {adults} adultos e {minors} menores.")
