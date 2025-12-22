# 044
# ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO,
# CONSIDERANDO O PREÇO NORMAL E A CONDIÇÃO DE PAGAMENTO:
# 	- À VISTA (DINHEIRO/CHEQUE):    10% DE DESCONTO
# 	- À VISTA (CARTÃO):             5% DE DESCONTO
# 	- PARCELADO (ATÉ 2X):           PREÇO NORMAL
# 	- PARCELADO (ACIMA DE 3X):      20% DE JUROS

from cli.io import printf
from cli.wait import wait


def run():
    msg = ""
    price = float(input("Preço do produto: R$ "))

    printf(
        "[A] À vista | [C] Cartão",
        start="\n",
    )
    payment = input("Forma de pagamento: ").strip().upper()

    match payment:
        case "A":
            msg = "Valor total: R$ {:.2f} (-10%)".format(price * 0.9)
        case "C":
            qnt = int(input("Quantidade de parcelas: "))

            if qnt == 1:
                msg = "Valor total: R$ {:.2f} (-5%)".format(price * 0.95)
            elif qnt == 2:
                msg = "Valor total: R$ {:.2f} 2x{:.2f}".format(
                    price,
                    price / 2,
                )
            else:
                total = price * 1.2
                msg = "Valor total: R$ {:.2f} 2x{:.2f}".format(
                    total,
                    total / qnt,
                )
        case _:
            msg = "Valor total: R$ {:.2f}".format(price)

    wait("Calculando...")
    printf(
        msg,
        style="bold",
        color="cyan",
    )


if __name__ == "__main__":
    run()
