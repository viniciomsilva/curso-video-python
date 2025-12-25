# 019
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do
# escolhido.

from random import choice

from cli.io import inputf_int
from cli.io import printf
from cli.ux import wait


def read_students(qnt: int = 4) -> list[str]:
    names: list[str] = []

    printf(
        "Agora digite os nomes deles",
        start="\n",
        style="bold",
        color="yellow",
    )

    for i in range(qnt):
        student = input("Nome do(a) {}º aluno(a): ".format(i + 1))
        names.append(student.title().strip())

    return names


if __name__ == "__main__":
    qnt_students = inputf_int("Digite a quantidade alunos: ")
    students: list[str] = read_students(qnt_students)

    # printf(
    #     "Agora digite os nomes deles",
    #     start="\n",
    #     style="bold",
    #     color="yellow",
    # )
    # for i in range(qnt_students):
    #     student = input("Nome do(a) {}º aluno(a): ".format(i + 1))
    #     students.append(student.title().strip())

    wait("Sorteando...")

    printf(
        "O(A) aluno(a) sorteado(a) foi: {}".format(choice(students)),
        style="bold",
        color="cyan",
    )
