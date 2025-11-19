# 071
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
# pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
# programa vai informar quantas cédulas de cada valor serão entregues.

# Obs.: Considere que o caixa possui cédulas de R$ 50,00, R$ 20,00, R$ 10,00 e
# R$ 1,00.

from cli.io import printf
from cli.wait import wait


def run():
    combination = {
        "50": 0,
        "20": 0,
        "10": 0,
        "2": 0,
        "1": 0,
    }
    msg = ""
    value = int(input("Valor a ser sacado: R$ "))

    wait("Calculando cédulas...")

    for i in combination.keys():
        combination[i] += value // int(i)
        value %= int(i)

        if combination[i] != 0:
            msg += f"\n{combination[i]} x R$ {i},00"

    printf(
        msg,
        style="bold",
        color="cyan",
    )
