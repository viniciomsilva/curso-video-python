# 019
# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.
# FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO
# ESCOLHIDO

from random import choice

from cli.io import printf
from cli.wait import wait


def run():
    students = []
    qnt_students = int(input("Digite a quantidade alunos: "))

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
        "O(A) aluno(a) sorteado(a) foi: {}".format(choice(students)),
        style="bold",
        color="cyan",
    )


if __name__ == "__main__":
    run()
