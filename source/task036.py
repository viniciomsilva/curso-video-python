# 036
# ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA
# CASA. O PROGRAMA DEVE PERGUNTAR O VALOR TOTAL DA CASA, O SALÁRIO DO COMPRADOR
# E EM QUANTOS ANOS ELE VAI PAGAR.
# CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER 30% DO
# SALÁRIO OU ENTÃO O EMPRÉSTIMO NÃO SERÁ APROVADO.

from time import sleep

from utils import custom as cs


def grant_loan(monthly_installment, salary):
    return monthly_installment <= (salary * 0.3)


def run():
    house_value = float(input("Digite o valor total do imóvel: R$ "))
    salary = float(input("Digite o salário do comprador: R$ "))
    years = float(input("Digite o quantidade de anos:    "))

    monthly_installment = house_value / years / 12

    print(cs.colorize("\nCalculando...\n", color="green"))
    sleep(1)

    if grant_loan(monthly_installment, salary):
        print(cs.colorize("Empréstimo aprovado!", color="cyan"))
    else:
        print(cs.colorize("Empréstimo negado!", color="lilac"))

    print(f"Parcela mensal de R$ {monthly_installment:.2f}")
    print(f"Equivale a {(monthly_installment / salary * 100):.1f}% da renda.")


if __name__ == "__main__":
    run()
