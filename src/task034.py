# 034
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor
# do seu aumento.
#   - Para salário acima de R$ 1250,00, calcule um aumento de 10%;
#   - Para os inferiores ou iguais, o aumento é de 15%.

from cli.io import inputf_flo
from cli.io import printf
from cli.ux import brl


def __calc(salary: float) -> float:
    return salary * 1.1 if salary > 1250 else salary * 1.15


if __name__ == "__main__":
    salary = inputf_flo("Digite o salário do funcionário: R$ ")

    printf(
        "O novo salário com ficará ".format(brl(__calc(salary))),
        start="\n",
        style="bold",
        color="cyan",
    )
