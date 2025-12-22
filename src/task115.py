# 115
# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu
# nome e idade num arquivo de texto simples.
# O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as
# pessoas cadastradas.

from cli.io import inputf
from cli.io import inputf_int
from cli.io import printf
from cli.wait import wait
from scripts.database import write
from scripts.database import read_csv
from scripts.terminal import clear


def __load() -> list[list[str | int]]:
    people = read_csv("people.txt")

    if people:
        return [[p[0], int(p[1])] for p in people]

    return []


def __menu():
    printf("Menu", end="\n\n", style="bold", color="cyan")
    print("[1] Ver pessoas")
    print("[2] Cadastrar pessoa")
    print("[3] Sair do sistema")


def __register(people: list[list[str | int]]):
    printf("Cadastrar pessoa", end="\n\n", style="bold", color="cyan")

    name = input("Nome: ").strip().title()
    birth = inputf_int("Ano de nascimento: ")

    people.append([name, birth])

    if write([name, birth], filename="people.txt", mode="a"):
        wait(f"🙌 {name} cadastrado(a) com sucesso...")


def __print_people(people: list[list[str | int]]):
    printf("Pessoas cadastradas", end="\n\n", style="bold", color="cyan")

    for p in people:
        print(f"Nome: {p[0]:<28} | Nascimento: {p[1]:6}")


def run():
    people = __load()

    while True:
        clear()
        __menu()

        op = inputf_int("Escolha uma opção >>> ", start="\n")

        match op:
            case 1:
                clear()
                __print_people(people)
                inputf("Pressione qualquer tecla para continuar...", start="\n")
            case 2:
                clear()
                __register(people)
            case 3:
                wait("👋 Sistema finalizado...")
                break
            case _:
                wait("🙁 Opção está indisponível!", color="cyan")


if __name__ == "__main__":
    run()
