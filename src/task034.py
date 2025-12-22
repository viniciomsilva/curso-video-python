# 034
# ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR
# DO SEU AUMENTO.
# PARA SALÁRIO ACIMA DE R$ 1250,00, CALCULE UM AUMENTO DE 10%.
# PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.

from cli.io import printf


def __calc(salary):
    return salary * 1.1 if salary > 1250 else salary * 1.15


def run():
    salary = float(input("Digite o salário do funcionário: R$ "))

    printf(
        "O novo salário com ficará R$ {:.2f}".format(__calc(salary)),
        start="\n",
        style="bold",
        color="cyan",
    )


if __name__ == "__main__":
    run()
