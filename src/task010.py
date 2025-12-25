# 010
# Crie um conversor de real para dólar.

from cli.io import inputf_flo
from cli.io import printf
from cli.ux import brl


# BCB in 5/9/25
__USD = 5.3962
__EUR = 6.3449


if __name__ == "__main__":
    value = inputf_flo("Digite um valor em R$: ")

    printf(
        "BRL {} = USD US{}".format(brl(value), brl(value / __USD, sing="$")),
        start="\n",
        style="bold",
        color="cyan",
    )
    printf(
        "BRL {} = EUR   €{}".format(brl(value), brl(value / __EUR, sing="")),
        style="bold",
        color="magenta",
    )
