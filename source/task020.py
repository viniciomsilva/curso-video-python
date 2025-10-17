# 020
# O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE
# TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E
# MOSTRE A ORDEM SORTEADA

from random import sample
from time import sleep

from utils import custom as cs


def reorder(data):
    return sample(data, len(data))


def run():
    students = []
    qnt_students = int(input("Digite a quantidade de alunos: "))

    print(cs.colorize("\nAgora digite o nome deles", color="yellow"))

    for i in range(qnt_students):
        student = input(f"Nome do(a) {(i + 1)}º aluno(a): ")
        students.append(student.title().strip())

    print(cs.colorize("\nSorteando...", color="green"))
    sleep(3)

    print(cs.colorize("\nOrdem sorteada", color="cyan"))

    for i, student in enumerate(reorder(students)):
        print(cs.bold(f"{(i + 1)}º aluno(a): {student}"))


if __name__ == "__main__":
    run()
