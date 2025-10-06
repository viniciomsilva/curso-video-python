# 030
# CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA SE ELE É
# PAR OU ÍMPAR.

if __name__ == "__main__":
    num = int(input("DIGITE UM NÚMERO INTEIRO QUALQUER: "))

    print("ESTE NÚMERO É PAR!" if num % 2 == 0 else "ESTE NÚMERO É ÍMPAR!")
