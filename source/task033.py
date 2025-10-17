# 033
# FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL O MENOR.

from utils import custom as cs


def run():
    numbers = []

    for i in range(3):
        numbers.append(int(input(f"Digite o {(i + 1)}º número: ")))

    print(cs.colorize(f" {max(numbers):<4} é o maior ", back="cyan"))
    print(cs.colorize(f" {min(numbers):<4} é o menor ", back="lilac"))


if __name__ == "__main__":
    run()
