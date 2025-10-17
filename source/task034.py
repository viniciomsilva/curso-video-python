# 034
# ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR
# DO SEU AUMENTO.
# PARA SALÁRIO ACIMA DE R$ 1250,00, CALCULE UM AUMENTO DE 10%.
# PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.

from utils import custom as cs


def new_salary(salary):
    return salary * 1.1 if salary > 1250 else salary * 1.15


def run():
    salary = float(input("Digite o salário do funcionário (R$): "))

    print(
        cs.colorize(
            f"O novo salário com ficará R$ {new_salary(salary):.2f}",
            color="cyan",
        )
    )


if __name__ == "__main__":
    run()
