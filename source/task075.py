# 075
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os numa
# tupla. No final, mostre:
#   - Quantas vezes apareceu o valor 9
#   - Em que posição foi digitado o primeiro valor 3
#   - Quais foram os números pares

from cli.io import EXIT_CMDS
from cli.io import inputf
from cli.io import printf


def run():
    msg = ""
    numbers = []

    while True:
        n = inputf("Digite um número inteiro: ", start="\n").strip()

        if not n.isnumeric():
            printf("Por favor! ", end="", color="red")
            continue

        numbers.append(int(n))

        if input("Quer adicionar outros? [S/N] ").lower().strip() in EXIT_CMDS:
            break

    pairs = set(filter(lambda n: n % 2 == 0, numbers))

    msg += f"O número 9 apareceu {numbers.count(9)} vezes!"
    if 3 in numbers:
        msg += f"\nO primeiro 3 está na {numbers.index(3) + 1}ª posição!"
    else:
        msg += "\nO números 3 não está na lista!"
    msg += "\nOs números pares são: {}!".format(", ".join(map(str, pairs)))

    printf(msg, start="\n")
