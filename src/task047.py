# 047
# CRIE UM PROGRAMA QUE MOSTRE TODOS OS NÚMEROS PARES NUM INTERVALO DE 1 A 50.

from cli.io import printf


def run():
    final = int(input("Até: "))

    print()
    for i in range(2, final + 1, 2):
        printf(f"{i}", end=" ", style="bold")

    printf(
        "Fim!",
        style="bold",
        color="green",
    )


if __name__ == "__main__":
    run()
