# 027
# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA
# O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE


def run():
    name = input("Digite o seu nome completo: ").strip().title().split()

    print("\nSeu primeiro nome é: {}".format(name[0]))
    print("Seu sobrenome é: {}".format(name[len(name) - 1]))
