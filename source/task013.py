# 013
# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE-O COM 15% DE
# AUMENTO

from utils import custom as cs


def calc_increase(salary, increase):
    return salary * (1 + increase / 100)


def run():
    salary = float(input("Digite o salário....: R$ "))
    increase = float(input("Digite o aumento (%):    "))

    print(
        cs.colorize(
            f"\nNovo salário: R$ {calc_increase(salary, increase):.2f}",
            color="cyan",
        )
    )


if __name__ == "__main__":
    run()
