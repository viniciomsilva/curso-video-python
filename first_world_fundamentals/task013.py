# 013
# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE-O COM 15% DE
# AUMENTO

from custom import customize


if __name__ == "__main__":
    salary = float(input("DIGITE O SALÁRIO....: R$ "))
    increase = float(input("DIGITE O AUMENTO (%):    "))

    print(
        "\nNOVO SALÁRIO........: {}R$ {:.2f}".format(
            customize(style="bold", color="cyan"),
            (salary * (1 + increase / 100)),
        )
    )
