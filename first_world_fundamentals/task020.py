# 020
# O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE
# TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E
# MOSTRE A ORDEM SORTEADA

from random import sample

students = []
drawnOrder = []

qntStudents = int(input("DIGITE A QUANTIDADE DE ALUNOS: "))

print("\nAGORA DIGITE OS SEUS NOMES")

for i in range(0, qntStudents):
    student = input("NOME DO ALUNO #{}: ".format((i + 1)))

    students.append(student)

drawnOrder = sample(students, len(students))

print(f"\n{'ORDEM SORTEADA ':-<40}\n")

for student in drawnOrder:
    print("ALUNO #{}: {}".format((drawnOrder.index(student) + 1), student))
