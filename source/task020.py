# 020
# O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE
# TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E
# MOSTRE A ORDEM SORTEADA

from random import sample
from time import sleep

from scripts.custom import customize


def reorder(data):
    return sample(data, len(data))


def run():
    students = []
    qnt_students = int(input("Digite a quantidade de alunos: "))

    print(
        customize(
            "\nAgora digite os nomes deles",
            style="bold",
            color="yellow",
        )
    )

    for i in range(qnt_students):
        student = input("Nome do(a) {}º aluno(a): ".format(i + 1))
        students.append(student.title().strip())

    print(customize("\nSorteando...", color="green"))
    sleep(3)

    print(
        customize(
            "\nOrdem sorteada",
            style="bold",
            color="cyan",
        )
    )

    for i, student in enumerate(reorder(students)):
        print(
            customize(
                "{}º aluno(a): {}".format(
                    i + 1,
                    student,
                ),
                style="bold",
            )
        )
