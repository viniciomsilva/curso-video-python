# 009
# Faça um programa que leia um número inteiro qualquer e mostre a sua tabuada.

# 049
# Refaça a tarefa 009, mostrando a tabuada utilizando o laço for/range.

# 067
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para
# cada valor digitado pelo usuário. O programa será interrompido quando o número
# for negativo.

from cli.io import printf
from cli.io import inputf
from cli.io import EXIT_CMDS
from scripts.terminal import clear


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
    while True:
        num = int(input("Digite um número: "))

        __add(num)
        __sub(num)
        __mul(num)
        __div(num)

        if (
            inputf(
                "Quer a tabuada de outro número? [S/N] ",
                start="\n",
                style="bold",
                color="yellow",
            )
            in EXIT_CMDS
        ):
            break

        clear()


if __name__ == "__main__":
    run()
