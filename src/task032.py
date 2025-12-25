# 032
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# - Regra dos bissextos:
#   - Para anos centenários: deve-se ser divisível por 400;
#   - Para anos normais: deve-se ser divisível por 4.

from cli.io import inputf_int
from cli.io import printf
from cli.ux import THIS_YEAR


def __calc(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


if __name__ == "__main__":
    year = inputf_int("Digite um ano qualquer (yyyy): ")

    year = year if year > 0 else THIS_YEAR

    if __calc(year):
        printf(
            "👍 {} é um ano bissexto!".format(year),
            start="\n",
            style="bold",
            color="cyan",
        )
    else:
        printf(
            "👎 {} NÃO é um ano bissexto!".format(year),
            start="\n",
            style="bold",
            color="magenta",
        )
