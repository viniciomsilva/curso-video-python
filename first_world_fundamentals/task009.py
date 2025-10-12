# 009
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE A SUA TABUADA


def print_add(num):
    print(f"\n{'ADIÇÃO ':-<26}\n")
    for i in range(1, 11):
        print("{} + {:2} = {}".format(num, i, (num + i)))


def print_sub(num):
    print(f"\n{'SUBTRAÇÃO ':-<26}\n")
    for i in range(1, 11):
        print("{} - {:2} = {}".format(num, i, (num - i)))


def print_mul(num):
    print(f"\n{'MULTIPLICAÇÃO ':-<26}\n")

    if num == 0:
        print("0 x  n = 0")
    else:
        for i in range(1, 11):
            print("{} x {:2} = {}".format(num, i, (num * i)))


def print_div(num):
    print(f"\n{'DIVISÃO ':-<26}\n")

    if num == 0:
        print("0 ÷  n = ε")
    else:
        for i in range(1, 11):
            print("{} ÷ {:2} = {:<6} |{}|".format(num, i, (num // i), (num % i)))


if __name__ == "__main__":
    num = int(input("DIGITE UM NÚMERO: "))

    print_add(num)
    print_sub(num)
    print_mul(num)
    print_div(num)
