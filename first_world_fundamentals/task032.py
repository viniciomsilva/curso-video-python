# 032
# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO.

# REGRA DOS BISSEXTOS
# PARA ANOS CENTENÁRIOS
#   DEVE-SE SER DIVISÍVEL POR 400
# PARA ANOS NORMAIS
#   DEVE-SE SER DIVISÍVEL POR 4


if __name__ == "__main__":
    year = int(input("DIGITE UM ANO QUALQUER (YYYY): "))

    print(
        "ESSE É UM ANO BISSEXTO"
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0
        else "ESSE NÃO É UM ANO BISSEXTO"
    )
