# 007
# DESENVOLVA UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE A SUA
# MÉDIA

grade1 = float(input("DIGITE A NOTA #1: "))
grade2 = float(input("DIGITE A NOTA #2: "))

average = (grade1 + grade2) / 2

if average >= 6:
    print("O ALUNO ESTÁ APROVADO COM MÉDIA {:.1f}".format(average))

elif 6 > average >= 3:
    print("O ALUNO ESTÁ DE RECUPERAÇÃO COM MÉDIA {:.1f}".format(average))

else:
    print("O ALUNO ESTÁ REPROVADO COM MÉDIA {:.1f}".format(average))
