# 020
# O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE
# TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E
# MOSTRE A ORDEM SORTEADA

from random import sample

from cli.io import printf
from cli.wait import wait


def __reorder(data):
    return sample(data, len(data))


def run():
    students = []
    qnt_students = int(input("Digite a quantidade de alunos: "))

    printf(
        "Agora digite os nomes deles",
        start="\n",
        style="bold",
        color="yellow",
    )
    for i in range(qnt_students):
        student = input("Nome do(a) {}º aluno(a): ".format(i + 1))
        students.append(student.title().strip())

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
