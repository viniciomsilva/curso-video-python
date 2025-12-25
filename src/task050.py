# 050
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

from cli.io import printf


if __name__ == "__main__":
    s = 0

    for i in range(6):
        n = int(input("{}º valor: ".format(i + 1)))

        if n % 2 == 0:
            s += i

    printf(
        "A soma dos valores pares é: {}".format(s),
        start="\n",
        style="bold",
        color="cyan",
    )
