# 023
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO ENTRE 0 E 9999 E MOSTRE CADA UM DOS
# DÍGITOS SEPARADOS

from classes.separate_number import SeparateNumber
from cli.io import printf


def run():
    while True:
        try:
            num = int(input("Digite um número inteiro qualquer: "))

            printf(
                "Este é o número separado em casas decimais",
                start="\n",
                style="bold",
                color="cyan",
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
            printf(
                "Por favor, digite um número válido!",
                style="bold",
                color="magenta",
            )
            printf(
                "Número inteiro e sem pontuações!",
                style="bold",
                color="yellow",
            )
            continue
