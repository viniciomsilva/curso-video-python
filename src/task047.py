# 047
# Crie um programa que mostre todos os números pares num intervalo de 1 a 50.

from cli.io import inputf_int
from cli.io import printf


if __name__ == "__main__":
    final = inputf_int("Até: ")

    print()
    for i in range(2, final + 1, 2):
        printf(f"{i}", end=" ", style="bold")

    printf(
        "Fim!",
        style="bold",
        color="green",
    )
