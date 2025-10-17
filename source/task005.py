# 005
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E
# ANTECESSOR

from utils import custom as cs


def run():
    num = int(input("Digite um número inteiro qualquer: "))

    print(cs.colorize(f" Antecessor: {(num - 1):4} ", back="cyan"))
    print(cs.colorize(f" Sucessor..: {(num + 1):4} ", back="lilac"))


if __name__ == "__main__":
    run()
