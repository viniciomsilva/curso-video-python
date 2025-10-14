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

from custom import clear
from custom import customize


if __name__ == "__main__":
    grade1 = float(input("Digite a 1ª nota: "))
    grade2 = float(input("Digite a 2ª nota: "))

    average = (grade1 + grade2) / 2

    print(
        "\n{}Calculando...{}".format(
            customize(style="bold", color="green"),
            clear(),
        )
    )
    sleep(1)

    if average >= 7:
        print(
            "{}Aluno(a) APROVADO(A) com média {:.1f}!".format(
                customize(style="bold", color="cyan"),
                average,
            )
        )
    elif 7 > average >= 5:
        print(
            "{}Aluno(a) DE RECUPERAÇÃO com média {:.1f}!".format(
                customize(style="bold", color="yellow"),
                average,
            )
        )
    else:
        print(
            "{}Aluno(a) REPROVADO(A) com média {:.1f}!".format(
                customize(style="bold", color="lilac"),
                average,
            )
        )
