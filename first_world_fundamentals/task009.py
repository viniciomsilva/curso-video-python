# 009
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE A SUA TABUADA

num = int(input("DIGITE UM NÚMERO: "))

print(f"\n{'ADIÇÃO ':-<26}\n")

for i in range(1, 11):
    print("{} + {:2} = {}".format(num, i, (num + i)))

print(f"\n{'SUBTRAÇÃO ':-<26}\n")

for i in range(1, 11):
    print("{} - {:2} = {}".format(num, i, (num - i)))

if num == 0:
    print(f"\n{'MULTIPLICAÇÃO ':-<26}\n")
    print("0 x  n = 0")
    print(f"\n{'DIVISÃO ':-<26}\n")
    print("0 ÷  n = ε")

else:
    print(f"\n{'MULTIPLICAÇÃO ':-<26}\n")

    for i in range(1, 11):
        print("{} x {:2} = {}".format(num, i, (num * i)))

    print(f"\n{'DIVISÃO ':-<26}\n")

    for i in range(1, 11):
        print("{} ÷ {:2} = {:<6} |{}|".format(num, i, (num // i), (num % i)))
