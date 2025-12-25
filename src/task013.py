# 013
# Faça um algoritmo que leia o salário de um funcionário e mostre-o com 15% de
# aumento.

from cli.io import inputf_flo
from cli.io import printf
from cli.ux import brl


def __calc(salary: float, increase: float) -> float:
    return salary * (1 + increase / 100)


if __name__ == "__main__":
    salary = inputf_flo("Digite o salário: R$ ")
    increase = inputf_flo("Digite o aumento (%): ")

    printf(
        "Novo salário: {}".format(brl(__calc(salary, increase))),
        start="\n",
        style="bold",
        color="cyan",
    )
