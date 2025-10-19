# 036
# ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA
# CASA. O PROGRAMA DEVE PERGUNTAR O VALOR TOTAL DA CASA, O SALÁRIO DO COMPRADOR
# E EM QUANTOS ANOS ELE VAI PAGAR.
# CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER 30% DO
# SALÁRIO OU ENTÃO O EMPRÉSTIMO NÃO SERÁ APROVADO.

from cli.io import printf
from cli.wait import wait


def __calc(monthly_installment, salary):
    return monthly_installment <= (salary * 0.3)


def run():
    house_value = float(input("Digite o valor total do imóvel: R$ "))
    salary = float(input("Digite o salário do comprador: R$ "))
    years = float(input("Digite o quantidade de anos: "))

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
        "Parcela mensal de R$ {:.2f}".format(
            monthly_installment,
        )
    )
    print(
        "Equivale a {:.1f}% da renda.".format(
            monthly_installment / salary * 100,
        )
    )
