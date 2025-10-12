# 020
# O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE
# TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E
# MOSTRE A ORDEM SORTEADA

from random import sample

from custom import clear
from custom import customize

if __name__ == "__main__":
    students = []
    drawn_order = []

    qnt_students = int(input("DIGITE A QUANTIDADE DE ALUNOS: "))

    print(
        "\n{}AGORA DIGITE OS NOMES DELES{}".format(
            customize(style="bold", color="yellow"),
            clear(),
        )
    )

    for i in range(qnt_students):
        student = input("NOME DO ALUNO #{}: ".format((i + 1)))
        students.append(student.upper().strip())

    drawn_order = sample(students, len(students))

    print(
        "\n{}ORDEM SORTEADA{}".format(
            customize(style="bold", color="cyan"),
            clear(),
        )
    )

    for i, student in enumerate(drawn_order):
        print(
            "{}ALUNO #{}: {}".format(
                customize(style="bold"),
                (i + 1),
                student,
            )
        )
