# 030
# Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é
# par ou ímpar.

from cli.io import inputf_int

if __name__ == "__main__":
    num = inputf_int("Digite um número inteiro qualquer: ")

    print("Este número é par!" if num % 2 == 0 else "Este número é ímpar!")
