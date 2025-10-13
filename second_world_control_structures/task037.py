# 037
# ESCREVA UM PROGRAMA QUE LEIA UM VALOR INTEIRO QUALQUER E PEÇA PARA O USUÁRIO
# ESCOLHER QUAL SERÁ A BASE NUMÉRICA DE CONVERSÃO:
# 	1 PARA BASE BINÁRIA
# 	2 PARA OCTAL
# 	3 PARA HEXADECIMAL

from time import sleep

from custom import bold
from custom import colorize


if __name__ == "__main__":
    print("Conversor decimal para:")
    print("[2] Binário - [8] Octal - [16] Hexadecimal")

    while True:
        try:
            num = int(input("\nDigite um número inteiro: "))
            base = int(input("Para qual base você quer converter? #"))

            print(colorize("\nCalculando...", "green"))
            sleep(1)

            match base:
                case 2:
                    print(bold(f"{num} em binário = {bin(num)[2:]}"))
                case 8:
                    print(bold(f"{num} em octal = {oct(num)[2:]}"))
                case 16:
                    print(bold(f"{num} em hexadecimal = {hex(num)[2:]}"))
                case _:
                    print(colorize("Base de conversão inválida!", "lilac"))
        except:
            print(colorize("Ops! Algo deu errado.", "red"))
        finally:
            if input("\nQuer converter outro? [y/n] ") != "y":
                break
