# 059
# Crie um programa que leia dois valores e mostre um menu.
#   [1] Somar
#   [2] Multiplicar
#   [3] Maior
#   [4] Novos valores
#   [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

# 064 & 066
# Crie um programa que leia vários números inteiros pelo teclado. O programa só
# vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles.
# Obs.: Desconsidere a flag.

# 065
# Crie um programa que leia vários números inteiros pelo teclado. No final da
# execução, mostre a média entre todos os valores e qual é o maior e o menor
# valores lidos. O programa deve perguntar ao usuário se ele quer ou não a
# digitar mais valores.

from math import prod
from statistics import mean
from time import sleep

from cli.io import printf
from cli.io import inputf
from cli.wait import wait
from scripts import terminal


__options = [
    "[1] Somar",
    "[2] Multiplicar",
    "[3] Maior",
    "[4] Menor",
    "[5] Média",
    "[6] Novos valores",
    "[7] Adicionar valores",
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
    printf(
        "Quantidade: {} números ".format(len(numbers)),
        style="bold",
        end="\n\n"
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
                rps = "A média é: {:.2f}".format(mean(numbers))
            case "6":
                numbers = []
                __add_new_values(numbers)
            case "7":
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
        sleep(2)


if __name__ == "__main__":
    run()
