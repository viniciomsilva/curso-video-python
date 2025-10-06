# 034
# ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR
# DO SEU AUMENTO.
# PARA SALÁRIO ACIMA DE R$ 1250,00, CALCULE UM AUMENTO DE 10%.
# PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.

if __name__ == "__main__":
    salary = float(input("DIGITE O SALÁRIO DO FUNCIONÁRIO (R$): "))

    print("O NOVO SALÁRIO COM REAJUSTE FICARÁ R$ {:.2f}".format(
        salary * 1.1 if salary > 1250 else salary * 1.15
    ))
