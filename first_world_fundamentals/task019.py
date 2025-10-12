# 019
# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.
# FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO
# ESCOLHIDO

from random import choice

from custom import customize


if __name__ == "__main__":
    students = []
    qnt_students = int(input("DIGITE A QUANTIDADE DE ALUNOS: "))

    print()

    for i in range(qnt_students):
        student = input(f"DIGITE O NOME DO(A) ALUNO(A) #{i + 1}: ")
        students.append(student.upper().strip())

    print(
        "\n{}O(A) ALUNO(A) SORTEADO(A) FOI...: {}".format(
            customize(style="bold", color="cyan"),
            choice(students),
        )
    )
