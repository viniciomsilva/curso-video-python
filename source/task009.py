# 009
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE A SUA TABUADA

from cli.io import printf


def __add(num):
    printf(
        "{:=<30}".format("Adição "),
        start="\n",
        end="\n\n",
        style="bold",
        color="cyan",
    )
    for i in range(1, 11):
        printf(
            "{} + {:2} = {}".format(num, i, num + i),
            style="bold",
        )


def __sub(num):
    printf(
        "{:=<30}".format("Subtração "),
        start="\n",
        end="\n\n",
        style="bold",
        color="yellow",
    )
    for i in range(1, 11):
        printf(
            "{} - {:2} = {}".format(num, i, num - i),
            style="bold",
        )


def __mul(num):
    printf(
        "{:=<30}".format("Multiplicação "),
        start="\n",
        end="\n\n",
        style="bold",
        color="magenta",
    )

    if num == 0:
        printf("0 x  n = 0", style="bold")
    else:
        for i in range(1, 11):
            printf(
                "{} x {:2} = {}".format(num, i, num * i),
                style="bold",
            )


def __div(num):
    printf(
        "{:=<30}".format("Divisão "),
        start="\n",
        end="\n\n",
        style="bold",
        color="green",
    )

    if num == 0:
        printf(
            "0 ÷  n = ε",
            style="bold",
            color="red",
        )
    else:
        for i in range(1, 11):
            printf(
                "{} ÷ {:2} = {:<6} |{}|".format(num, i, num // i, num % i),
                style="bold",
            )


def run():
    num = int(input("Digite um número: "))

    __add(num)
    __sub(num)
    __mul(num)
    __div(num)
