# 027
# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA
# O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE


def run():
    name = input("Digite o seu nome completo: ").strip().title().split()

    print(f"Seu primeiro nome é: {name[0]}")
    print(f"Seu sobrenome é: {name[(len(name) - 1)]}")


if __name__ == "__main__":
    run()
