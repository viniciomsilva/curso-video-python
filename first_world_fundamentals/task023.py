# 023
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO ENTRE 0 E 9999 E MOSTRE CADA UM DOS
# DÍGITOS SEPARADOS

from classes.separate_number import SeparateNumber
from custom import clear
from custom import customize


if __name__ == "__main__":
    while True:
        try:
            value = int(input("DIGITE UM NÚMERO INTEIRO QUALQUER: "))

            print(
                "\n{}ESTE É O NÚMERO {} SEPARADO EM CASAS DECIMAIS!{}".format(
                    customize(style="bold", color="cyan"), value, clear()
                )
            )
            for digit in SeparateNumber(value).separated:
                print("{}: {}".format(digit["decimal_order"], digit["digit"]))

            break

        except:
            print(
                "{}POR FAVOR, DIGITE UM NÚMERO VÁLIDO!{}".format(
                    customize(style="bold", color="red"), clear()
                )
            )
            print(
                "{}NÚMERO INTEIRO E SEM PONTUAÇÕES!{}\n".format(
                    customize(style="bold", color="yellow"), clear()
                )
            )

            continue
