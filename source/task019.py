# 019
# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.
# FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO
# ESCOLHIDO

from random import choice
from time import sleep

from scripts.custom import customize


def run():
    students = []
    qnt_students = int(input("Digite a quantidade alunos: "))

    print()

    for i in range(qnt_students):
        student = input("Digite o nome do(a) {}º aluno(a): ".format(i + 1))
        students.append(student.title().strip())

    print(customize("\nSorteando...", color="green"))
    sleep(2)

    print(
        customize(
            "\nO(A) aluno(a) sorteado(a) foi: {}".format(
                choice(students),
            ),
            style="bold",
            color="cyan",
        )
    )
