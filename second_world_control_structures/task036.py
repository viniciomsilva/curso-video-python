# 036
# ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA
# CASA. O PROGRAMA DEVE PERGUNTAR O VALOR TOTAL DA CASA, O SALÁRIO DO COMPRADOR
# E EM QUANTOS ANOS ELE VAI PAGAR.
# CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER 30% DO
# SALÁRIO OU ENTÃO O EMPRÉSTIMO NÃO SERÁ APROVADO.

from time import sleep

from custom import colorize


if __name__ == "__main__":
    house_value = float(input("Digite o valor total do imóvel: R$ "))
    salary = float(input("Digite o salário do comprador.: R$ "))
    years = float(input("Digite o quantidade de anos...:    "))

    monthly_installment = house_value / years / 12

    print("\n{}".format(colorize("Calculando...", "green")))
    sleep(1)

    if monthly_installment > (salary * 0.3):
        print("\n{}".format(colorize("Empréstimo negado!", "lilac")))
    else:
        print("\n{}".format(colorize("Empréstimo aprovado!", "cyan")))

    print(
        "Parcela mensal de R$ {:.2f}".format(
            monthly_installment,
        )
    )
    print(
        "Equivalente a {:.2f}% da renda.".format(
            monthly_installment / salary * 100,
        )
    )
