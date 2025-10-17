# 006
# CRIE UM PROGRAMA QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, O TRIPLO E A RAIZ
# QUADRADA

from math import sqrt

from utils import custom as cs


def run():
    num = int(input("Digite um número inteiro: "))

    print(cs.colorize(f" Dobro........: {(num * 2):8} ", back="cyan"))
    print(cs.colorize(f" Triplo.......: {(num * 3):8} ", back="lilac"))
    print(cs.colorize(f" Raiz Quadrada: {sqrt(num):8} ", back="yellow"))


if __name__ == "__main__":
    run()
