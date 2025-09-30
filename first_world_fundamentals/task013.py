# 013
# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE-O COM 15% DE
# AUMENTO

salary = float(input("DIGITE O SALÁRIO....: R$ "))
increase = float(input("DIGITE O AUMENTO (%):    "))

print(
    "\nNOVO SALÁRIO........: R$ {:.2f}".format(
        (salary * (1 + increase / 100))
    )
)
