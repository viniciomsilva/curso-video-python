# 052
# Faça um programa que leia um número inteiro e mostre se ele é ou não um número
# primo.

from math import sqrt

from cli.io import printf


def __isprime(n):
    if n < 2:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def run():
    rps = {"content": "", "color": ""}
    num = int(input("Digite o número: "))

    rps["content"] = "O número {} ".format(num)

    if __isprime(num):
        rps["color"] = "cyan"
        rps["content"] += "É PRIMO!"
    else:
        rps["color"] = "magenta"
        rps["content"] += "NÃO É PRIMO!"

    printf(
        rps["content"],
        start="\n",
        style="bold",
        color=rps["color"],
    )
