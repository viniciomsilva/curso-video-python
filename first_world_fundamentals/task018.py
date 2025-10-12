# 018
# FAÇA UM PROGRAMA QUE LEIA O VALOR DE UM ÂNGULO QUALQUER E MOSTRE NA TELA OS
# VALORES DO SENO, COSSENO E TANGENTE

from math import cos
from math import radians
from math import sin
from math import tan

from custom import clear
from custom import customize


if __name__ == "__main__":
    angle = float(input("DIGITE UM ÂNGULO: "))

    print(
        "{} SIN({:.1f}º) = {:.6f} {}".format(
            customize(style="bold", back="cyan"),
            angle,
            sin(radians(angle)),
            clear(),
        )
    )
    print(
        "{} COS({:.1f}º) = {:.6f} {}".format(
            customize(style="bold", back="lilac"),
            angle,
            cos(radians(angle)),
            clear(),
        )
    )
    print(
        "{} TAN({:.1f}º) = {:.6f} {}".format(
            customize(style="bold", back="yellow"),
            angle,
            tan(radians(angle)),
            clear(),
        )
    )
