# 070
# Crie um programa que leia o nome e preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar. No final, mostre:
#   - Qual é o total gasto na compra;
#   - Quantos produtos custam mais de R$ 1.000,00;
#   - Qual é o nome do produto mais barato.

from cli.io import inputf
from cli.io import inputf_flo
from cli.io import leave
from cli.io import printf
from cli.ux import brl


if __name__ == "__main__":
    total = 0
    expensive = 0
    cheap = 0
    name_cheapest = ""

    while True:
        name = inputf("Nome do produto: ", start="\n").strip()
        price = inputf_flo("Preço do produto: R$ ")

        total += price

        if price > 1000:
            expensive += 1

        if price < cheap or cheap == 0:
            cheap = price
            name_cheapest = name

        if leave(
            "Quer continuar? [S/N] ",
            color="yellow",
        ):
            break

    rps = f"Total: {brl(total)}"
    rps += f"\nQuantidade de produtos caros: {expensive}"
    rps += f"\nProduto mais barato: {name_cheapest} ({brl(cheap)})"

    printf(
        rps,
        start="\n",
        style="bold",
        color="cyan",
    )
