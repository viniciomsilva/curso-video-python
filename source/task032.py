# 032
# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO.

# REGRA DOS BISSEXTOS
# PARA ANOS CENTENÁRIOS
#   DEVE-SE SER DIVISÍVEL POR 400
# PARA ANOS NORMAIS
#   DEVE-SE SER DIVISÍVEL POR 4


from datetime import date

from utils import custom as cs


def run():
    year = int(input("Digite um ano qualquer (yyyy): "))

    year = year if year >= 0 else date.today().year

    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print(
            cs.colorize(
                f"{year} é um ano bissexto!",
                color="cyan",
            )
        )
    else:
        print(
            cs.colorize(
                f"{year} NÃO é um ano bissexto!",
                color="lilac",
            )
        )


if __name__ == "__main__":
    run()
