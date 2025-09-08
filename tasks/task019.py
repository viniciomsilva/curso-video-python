# 019
# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.
# FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO

from random import choice #, randint

students = []
# selectedStudent = 0

qntStudents = int(input('DIGITE A QUANTIDADE DE ESTUDANTES: '))

print()

for i in range(0, qntStudents):
    student = input('DIGITE NO NOME DO ALUNO #{}: '.format((i + 1)))

    students.append(student)

# selectedStudent = randint(0, (len(students) - 1))

print('\nO ALUNO SORTEADO FOI......:', choice(students))
