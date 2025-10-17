# 019
# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.
# FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO
# ESCOLHIDO

from random import choice
from time import sleep

from utils import custom as cs


def run():
    students = []
    qnt_students = int(input("Digite a quantidade alunos: "))

    print()

    for i in range(qnt_students):
        student = input(f"Digite o nome do(a) {(i + 1)}º aluno(a): ")
        students.append(student.title().strip())

    print(cs.colorize("\nSorteando...", color="green"))
    sleep(2)

    print(
        "\n{}O(A) aluno(a) sorteado(a) foi: {}".format(
            cs.customize(style="bold", color="cyan"),
            choice(students),
        )
    )


if __name__ == "__main__":
    run()
