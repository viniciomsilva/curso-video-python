# 038
# Escreva um programa que leia dois valores inteiros compare-os, mostrando na
# tela uma mensagem:
#   - O primeiro valor é maior;
#   - O segundo valor é maior;
#   - Não existe maior, os dois são iguais.

from cli.io import inputf_int


if __name__ == "__main__":
    num1 = inputf_int("Digite o 1º valor: ")
    num2 = inputf_int("Digite o 2º valor: ")

    if num1 == num2:
        print("Ambos os valores são iguais!")
    elif num1 > num2:
        print("{} é maior que {}".format(num1, num2))
    else:
        print("{} é maior que {}".format(num2, num1))
