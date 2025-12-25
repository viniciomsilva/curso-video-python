# 036
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma
# casa. o programa deve perguntar o valor total da casa, o salário do comprador
# e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
# salário ou então o empréstimo não será aprovado.

from cli.io import inputf_flo
from cli.io import printf
from cli.ux import wait
from cli.ux import brl


def __calc(monthly_installment: float, salary: float) -> bool:
    return monthly_installment <= (salary * 0.3)


def run():
    house_value = inputf_flo("Digite o valor total do imóvel: R$ ")
    salary = inputf_flo("Digite o salário do comprador: R$ ")
    years = inputf_flo("Digite o quantidade de anos: ")

    monthly_installment = house_value / years / 12

    wait("Calculando...")

    if __calc(monthly_installment, salary):
        printf(
            "👍 Empréstimo APROVADO!",
            style="bold",
            color="cyan",
        )
    else:
        printf(
            "👎 Empréstimo NEGADO!",
            style="bold",
            color="magenta",
        )

    print(
        "Parcela mensal de {}".format(
            brl(monthly_installment),
        )
    )
    print(
        "Equivale a {:.1f}% da renda.".format(
            monthly_installment / salary * 100,
        )
    )


if __name__ == "__main__":
    run()
