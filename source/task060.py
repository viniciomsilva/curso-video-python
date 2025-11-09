# 060
# Faça um programa que leia um número qualquer e mostre o fatorial.
#   Ex.: 5! => 5 * 4 * 3 * 2 * 1 => 120

from math import factorial

from cli.io import printf
from cli.wait import wait


def run():
    msg = ""
    num = int(input("Digite um número: "))

    msg = "{}! = ".format(num)
    for i in range(num, 0, -1):
        msg += f"{i} * " if i != 1 else f"{i} = {factorial(num)}"

    wait("Calculando...")
    printf(
        msg,
        style="bold",
        color="cyan",
    )
