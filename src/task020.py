# 020
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de
# trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e
# mostre a ordem sorteada.

from random import sample

from cli.io import inputf_int
from cli.io import printf
from cli.ux import wait
from task019 import read_students


def __reorder(data: list[str]) -> list[str]:
    return sample(data, len(data))


if __name__ == "__main__":
    qnt_students = inputf_int("Digite a quantidade de alunos: ")
    students: list[str] = read_students(qnt_students)

    wait("Sorteando...")

    printf(
        "Ordem sorteada",
        style="bold",
        color="cyan",
    )
    for i, student in enumerate(__reorder(students)):
        printf(
            "{}º aluno(a): {}".format(i + 1, student),
            style="bold",
        )
