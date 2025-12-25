# 052
# Faça um programa que leia um número inteiro e mostre se ele é ou não um número
# primo.

from math import sqrt

from cli.io import inputf_int
from cli.io import printf


def __is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    rps = {"content": "", "color": ""}
    num = inputf_int("Digite o número: ")

    rps["content"] = f"O número {num} "

    if __is_prime(num):
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
