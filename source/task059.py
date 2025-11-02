# 059
# Crie um programa que leia dois valores e mostre um menu.
#   [1] Somar
#   [2] Multiplicar
#   [3] Maior
#   [4] Novos valores
#   [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from math import prod

from cli.io import printf
from cli.io import inputf
from cli.wait import wait
from scripts import terminal


__options = [
    "[1] Somar",
    "[2] Multiplicar",
    "[3] Maior",
    "[4] Menor",
    "[5] Novos valores",
    "[6] Adicionar valores",
    "[0] Sair",
]


def __add_new_values(numbers: list):
    while True:
        n = inputf("Qual valor quer adicionar? ").strip()

        if not n.isnumeric():
            printf(
                "Digite um valor inteiro...",
                style="bold",
                color="magenta",
            )
        elif n == "0":
            break
        else:
            numbers.append(int(n))

    terminal.clear()


def __print_numbers(numbers: list):
    printf(
        "Valores: ",
        start="\n",
        end="",
        style="bold",
    )
    printf(
        ", ".join(map(str, numbers)),
        style="bold",
    )


def __print_menu():
    print(" ".join(__options))


def run():
    numbers = []
    rps = ""

    __add_new_values(numbers)

    while True:
        __print_numbers(numbers)
        __print_menu()
        option = inputf("Digite a opção: ", start="\n").strip()

        wait("Processando...", end="\n")

        match option:
            case "1":
                rps = "A soma é: {}".format(sum(numbers))
            case "2":
                rps = "A multiplicação é: {}".format(prod(numbers))
            case "3":
                rps = "O maior valor é: {}".format(max(numbers))
            case "4":
                rps = "O menor valor é: {}".format(min(numbers))
            case "5":
                numbers = []
                __add_new_values(numbers)
            case "6":
                __add_new_values(numbers)
            case "0":
                break
            case _:
                printf(
                    "Opção inválida!",
                    style="bold",
                    color="magenta",
                )
                continue

        printf(
            rps,
            style="bold",
            color="cyan",
        )
