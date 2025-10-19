# 009
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE A SUA TABUADA


def print_add(num):
    print("\n{:=<30}\n".format("ADIÇÃO "))
    for i in range(1, 11):
        print(
            "{} + {:2} = {}".format(
                num,
                i,
                num + i,
            )
        )


def print_sub(num):
    print("\n{:=<30}\n".format("SUBTRAÇÃO "))
    for i in range(1, 11):
        print(
            "{} - {:2} = {}".format(
                num,
                i,
                num - i,
            )
        )


def print_mul(num):
    print("\n{:=<30}\n".format("MULTIPLICAÇÃO "))

    if num == 0:
        print("0 x  n = 0")
    else:
        for i in range(1, 11):
            print(
                "{} x {:2} = {}".format(
                    num,
                    i,
                    num * i,
                )
            )


def print_div(num):
    print("\n{:=<30}\n".format("DIVISÃO "))

    if num == 0:
        print("0 ÷  n = ε")
    else:
        for i in range(1, 11):
            print(
                "{} ÷ {:2} = {:<6} |{}|".format(
                    num,
                    i,
                    num // i,
                    num % i,
                )
            )


def run():
    num = int(input("Digite um número: "))

    print_add(num)
    print_sub(num)
    print_mul(num)
    print_div(num)
