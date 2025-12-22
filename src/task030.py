# 030
# CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA SE ELE É
# PAR OU ÍMPAR.


def run():
    num = int(input("Digite um número inteiro qualquer: "))

    print("Este número é par!" if num % 2 == 0 else "Este número é ímpar!")


if __name__ == "__main__":
    run()
