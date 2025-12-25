# 048
# Faça um programa que some todos o números ímpares múltiplos de três num
# intervalo de 1 a 500.

from cli.io import inputf_int
from cli.io import printf


if __name__ == "__main__":
    s = 0
    num = inputf_int("Até: ")

    for i in range(1, num + 1, 2):
        if i % 3 == 0:
            s += i

    printf(
        "A soma dos números ímpares múltiplos de 3 entre 1 e {}: {}".format(
            num,
            s,
        ),
        style="bold",
        color="cyan",
    )
