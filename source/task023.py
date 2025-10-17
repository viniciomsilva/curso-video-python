# 023
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO ENTRE 0 E 9999 E MOSTRE CADA UM DOS
# DÍGITOS SEPARADOS

from utils import SeparateNumber
from utils import custom as cs


def run():
    while True:
        try:
            value = int(input("Digite um número inteiro qualquer: "))

            print(
                cs.colorize(
                    "\nEste é o número separado em casas decimais",
                    color="cyan",
                )
            )
            for digit in SeparateNumber(value).separated:
                print("{}: {}".format(digit["decimal_order"], digit["digit"]))

            break
        except:
            print(
                cs.colorize(
                    "Por favor, digite um número válido!",
                    color="red",
                )
            )
            print(
                cs.colorize(
                    "Número inteiro e sem pontuações!",
                    color="yellow",
                )
            )

            continue


if __name__ == "__main__":
    run()
