# 038
# ESCREVA UM PROGRAMA QUE LEIA DOIS VALORES INTEIROS COMPARE-OS, MOSTRANDO NA
# TELA UMA MENSAGEM:
# 	- O PRIMEIRO VALOR É MAIOR
# 	- O SEGUNDO VALOR É MAIOR
# 	- NÃO EXISTE MAIOR, OS DOIS SÃO IGUAIS


def run():
    num1 = int(input("Digite o 1º valor: "))
    num2 = int(input("Digite o 2º valor: "))

    if num1 == num2:
        print("Ambos os valores são iguais!")
    elif num1 > num2:
        print("{} é maior que {}".format(num1, num2))
    else:
        print("{} é maior que {}".format(num2, num1))
