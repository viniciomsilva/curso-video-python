# 023
# Faça um programa que leia um número entre 0 e 9999 e mostre cada um dos
# dígitos separados.

from classes.separate_number import SeparateNumber
from cli.io import inputf_int
from cli.io import printf


if __name__ == "__main__":
    try:
        num = inputf_int("Digite um número inteiro qualquer: ")

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
    except Exception as e:
        printf(e, style="bold", color="magenta")
