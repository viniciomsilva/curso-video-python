# 032
# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO.

# REGRA DOS BISSEXTOS
# PARA ANOS CENTENÁRIOS
#   DEVE-SE SER DIVISÍVEL POR 400
# PARA ANOS NORMAIS
#   DEVE-SE SER DIVISÍVEL POR 4


from datetime import date

from custom import customize


if __name__ == "__main__":
    year = int(input("DIGITE UM ANO QUALQUER (YYYY): "))

    year = year if (year >= 0) else date.today().year

    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print(
            "{}{} É UM ANO BISSEXTO!".format(
                customize(style="bold", color="cyan"),
                year,
            )
        )
    else:
        print(
            "{}{} NÃO É UM ANO BISSEXTO!".format(
                customize(style="bold", color="lilac"),
                year,
            )
        )
