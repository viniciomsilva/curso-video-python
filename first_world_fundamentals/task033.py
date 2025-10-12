# 033
# FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL O MENOR.

from custom import clear
from custom import customize

if __name__ == "__main__":
    numbers = []

    for i in range(3):
        numbers.append(int(input(f"DIGITE O {(i + 1)}º NÚMERO: ")))

    print(
        "{} {:<4} É O MAIOR {}".format(
            customize(style="bold", back="cyan"),
            max(numbers),
            clear(),
        )
    )
    print(
        "{} {:<4} É O MENOR {}".format(
            customize(style="bold", back="lilac"),
            min(numbers),
            clear(),
        )
    )
