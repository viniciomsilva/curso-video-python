# 013
# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE-O COM 15% DE
# AUMENTO

from scripts.custom import customize


def calc_increase(salary, increase):
    return salary * (1 + increase / 100)


def run():
    salary = float(input("Digite o salário: R$ "))
    increase = float(input("Digite o aumento (%): "))

    print(
        customize(
            "\nNovo salário: R$ {:.2f}".format(
                calc_increase(salary, increase),
            ),
            style="bold",
            color="cyan",
        )
    )
