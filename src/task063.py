# 063
# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os
# n primeiros elementos duma Sequência de Fibonacci.
#   Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 ...

from cli.io import inputf_int
from cli.ux import wait


if __name__ == "__main__":
    p = 0
    c = 1
    seq = [p, c]
    n = inputf_int("Quantos números da sequência? ")

    for i in range(2, n):
        seq.append(p + c)
        p = c
        c = seq[i]

    wait("Calculando...")
    print("{}, Fim. Razão: {:.3f}".format(", ".join(map(str, seq)), (c / p)))
