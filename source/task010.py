# 010
# CRIEI UM CONVERSOR DE REAL PARA DÓLAR


def run():
    # BCB in 5/9/25
    brl_usd = 5.3962
    brl_eur = 6.3449

    brl = float(input("Digite um valor em R$: "))

    print(
        "BRL R$ {:.4f} = USD US$ {:.4f}".format(
            brl,
            brl / brl_usd,
        )
    )
    print(
        "BRL R$ {:.4f} = EUR   € {:.4f}".format(
            brl,
            brl / brl_eur,
        )
    )
