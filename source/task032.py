# 032
# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO.

# REGRA DOS BISSEXTOS
# PARA ANOS CENTENÁRIOS
#   DEVE-SE SER DIVISÍVEL POR 400
# PARA ANOS NORMAIS
#   DEVE-SE SER DIVISÍVEL POR 4


from datetime import date

from scripts.custom import customize


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def run():
    year = int(input("Digite um ano qualquer (yyyy): "))

    year = year if year > 0 else date.today().year

    if is_leap_year(year):
        print(
            customize(
                "{} é um ano bissexto!".format(year),
                style="bold",
                color="cyan",
            )
        )
    else:
        print(
            customize(
                "{} NÃO é um ano bissexto!".format(year),
                style="bold",
                color="magenta",
            )
        )
