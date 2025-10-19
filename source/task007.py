# 007
# DESENVOLVA UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE A SUA
# MÉDIA

# 040
# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO, CALCULE A MÉDIA E MOSTRE A
# SITUAÇÃO DELE DE ACORDO COM A MÉDIA
# 	- ABAIXO DE 5.0:	REPROVADO
# 	- ENTRE 5.0 E 6.9:	RECUPERAÇÃO
# 	- ACIMA DE 7.0:		APROVADO

from time import sleep

from scripts.custom import customize


def run():
    grade1 = float(input("Digite a 1ª nota: "))
    grade2 = float(input("Digite a 2ª nota: "))

    average = (grade1 + grade2) / 2

    print(customize("\nCalculando...\n", style="bold", color="green"))
    sleep(1)

    if average >= 7:
        print(
            customize(
                "Aluno(a) APROVADO(A) com média {:.1f}!".format(
                    average,
                ),
                style="bold",
                color="cyan",
            )
        )
    elif 7 > average >= 5:
        print(
            customize(
                "Aluno(a) DE RECUPERAÇÃO com média {:.1f}!".format(
                    average,
                ),
                style="bold",
                color="yellow",
            )
        )
    else:
        print(
            customize(
                "Aluno(a) REPROVADO(A) com média {:.1f}!".format(
                    average,
                ),
                style="bold",
                color="magenta",
            )
        )
