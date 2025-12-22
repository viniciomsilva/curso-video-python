# 070
# Crie um programa que leia o nome e preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar. No final, mostre:
#   - Qual é o total gasto na compra;
#   - Quantos produtos custam mais de R$ 1.000,00;
#   - Qual é o nome do produto mais barato.

from cli.io import EXIT_CMDS
from cli.io import inputf
from cli.io import printf


def run():
    total = 0
    expensive = 0
    cheap = 0
    name_cheapest = ""

    while True:
        name = inputf("Nome do produto: ", start="\n")
        price = float(input("Preço do produto: R$ "))

        total += price

        if price > 1000:
            expensive += 1

        if price < cheap or cheap == 0:
            cheap = price
            name_cheapest = name

        if (
            inputf(
                "Quer continuar? [S/N] ",
                color="yellow",
            ).strip()
            in EXIT_CMDS
        ):
            break

    rps = f"Total: R$ {total:.2f}"
    rps += f"\nQuantidade de produtos caros: {expensive}"
    rps += f"\nProduto mais barato: {name_cheapest} (R$ {cheap:.2f})"

    printf(
        rps,
        start="\n",
        style="bold",
        color="cyan",
    )


if __name__ == "__main__":
    run()
