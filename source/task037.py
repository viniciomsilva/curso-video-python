# 037
# ESCREVA UM PROGRAMA QUE LEIA UM VALOR INTEIRO QUALQUER E PEÇA PARA O USUÁRIO
# ESCOLHER QUAL SERÁ A BASE NUMÉRICA DE CONVERSÃO:
# 	1 PARA BASE BINÁRIA
# 	2 PARA OCTAL
# 	3 PARA HEXADECIMAL

from time import sleep

from utils import custom as cs


def run():
    print("Conversor decimal para:")
    print("[2] Binário - [8] Octal - [16] Hexadecimal")

    while True:
        try:
            num = int(input("\nDigite um número inteiro: "))
            base = int(input("Para qual base você quer converter? #"))

            print(cs.colorize("\nCalculando...\n", "green"))
            sleep(1)

            match base:
                case 2:
                    print(cs.bold(f"{num} em binário = {bin(num)[2:]}"))
                case 8:
                    print(cs.bold(f"{num} em octal = {oct(num)[2:]}"))
                case 16:
                    print(cs.bold(f"{num} em hexadecimal = {hex(num)[2:]}"))
                case _:
                    print(cs.colorize("Base de conversão inválida!", "lilac"))
        except:
            print(cs.colorize("Ops! Algo deu errado.", "red"))
        finally:
            if input("\nQuer converter outro? [y/n] ") != "y":
                break


if __name__ == "__main__":
    run()
