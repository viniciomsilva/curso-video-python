# 027
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o ultimo nome separadamente.

if __name__ == "__main__":
    name = input("Digite o seu nome completo: ").strip().title().split(" ")

    print("\nSeu primeiro nome é: {}".format(name[0]))
    print("Seu sobrenome é: {}".format(name[-1]))
