# 010
# CRIEI UM CONVERSOR DE REAL PARA DÓLAR

from cli.io import printf


# BCB in 5/9/25
__USD = 5.3962
__EUR = 6.3449


def run():
    brl = float(input("Digite um valor em R$: "))

    printf(
        "BRL R$ {:.4f} = USD US$ {:.4f}".format(brl, brl / __USD),
        start="\n",
        style="bold",
        color="cyan",
    )
    printf(
        "BRL R$ {:.4f} = EUR   € {:.4f}".format(brl, brl / __EUR),
        style="bold",
        color="magenta",
    )


if __name__ == "__main__":
    run()
