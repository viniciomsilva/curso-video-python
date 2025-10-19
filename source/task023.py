# 023
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO ENTRE 0 E 9999 E MOSTRE CADA UM DOS
# DÍGITOS SEPARADOS

from classes.separate_number import SeparateNumber
from scripts.custom import customize


def run():
    while True:
        try:
            num = int(input("Digite um número inteiro qualquer: "))

            print(
                customize(
                    "\nEste é o número separado em casas decimais",
                    style="bold",
                    color="cyan",
                )
            )
            for digit in SeparateNumber(num).separated:
                print(
                    "{}: {}".format(
                        str(digit["decimal_order"]).title(),
                        digit["digit"],
                    )
                )
            break
        except:
            print(
                customize(
                    "Por favor, digite um número válido!",
                    style="bold",
                    color="magenta",
                )
            )
            print(
                customize(
                    "Número inteiro e sem pontuações!",
                    style="bold",
                    color="yellow",
                )
            )
            continue
