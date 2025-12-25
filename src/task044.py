# 044
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o preço normal e a condição de pagamento:
#   - À vista (dinheiro/cheque):    10% de desconto;
#   - À vista (cartão):             5% de desconto;
#   - Parcelado (até 2x):           preço normal;
#   - Parcelado (acima de 3x):      20% de juros.

from cli.io import inputf_flo
from cli.io import printf
from cli.ux import wait
from cli.ux import brl


if __name__ == "__main__":
    msg = ""
    price = inputf_flo("Preço do produto: R$ ")

    printf(
        "[A] À vista | [C] Cartão",
        start="\n",
    )
    payment = input("Forma de pagamento: ").strip().upper()

    match payment:
        case "A":
            msg = f"Valor total: {brl(price * 0.9)} (-10%)"
        case "C":
            qnt = int(input("Quantidade de parcelas: "))

            if qnt == 1:
                msg = f"Valor total: {brl(price * 0.95)} (-5%)"
            elif qnt == 2:
                msg = f"Valor total: {brl(price)} 2x {brl(price / 2)}"
            else:
                total = price * 1.2
                msg = f"Valor total: {brl(total)} 2x {brl(total / qnt)}"
        case _:
            msg = f"Valor total: {brl(price)}"

    wait("Calculando...")
    printf(
        msg,
        style="bold",
        color="cyan",
    )
