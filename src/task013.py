# 013
# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE-O COM 15% DE
# AUMENTO

from cli.io import printf


def __calc(salary, increase):
    return salary * (1 + increase / 100)


def run():
    salary = float(input("Digite o salário: R$ "))
    increase = float(input("Digite o aumento (%): "))

    printf(
        "Novo salário: R$ {:.2f}".format(__calc(salary, increase)),
        start="\n",
        style="bold",
        color="cyan",
    )


if __name__ == "__main__":
    run()
