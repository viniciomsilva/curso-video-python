# 006
# CRIE UM PROGRAMA QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, O TRIPLO E A RAIZ
# QUADRADA

from math import sqrt

from custom import clear
from custom import customize

if __name__ == "__main__":
    num = int(input("DIGITE UM NÚMERO INTEIRO: "))

    print(
        "{} DOBRO........: {:8} {}".format(
            customize(style="bold", back="cyan"),
            (num * 2),
            clear(),
        )
    )
    print(
        "{} TRIPLO.......: {:8} {}".format(
            customize(style="bold", back="lilac"),
            (num * 3),
            clear(),
        )
    )
    print(
        "{} RAIZ QUADRADA: {:8.2f} {}".format(
            customize(style="bold", back="yellow"),
            sqrt(num),
            clear(),
        )
    )
