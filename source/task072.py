# 072
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extenso de zero até vinte. Seu programa deverá ler um número pelo teclado
# (entre 0 e 20) e mostrá-lo por extenso.

from scripts.database import read_csv


def run():
    numbers = tuple(data[0] for data in read_csv("numbers_in_words.csv"))

    while True:
        i = int(input("Digite um número entre 0 e 20: "))

        if 0 <= i <= 20:
            break

        print("Por favor! ", end="")

    print(f"Você digitou o número {numbers[i]}")
