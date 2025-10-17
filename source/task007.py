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

from utils import custom as cs


def run():
    grade1 = float(input("Digite a 1ª nota: "))
    grade2 = float(input("Digite a 2ª nota: "))

    average = (grade1 + grade2) / 2

    print(cs.colorize("\nCalculando...\n", color="green"))
    sleep(1)

    if average >= 7:
        print(
            cs.colorize(
                f"Aluno(a) APROVADO(A) com média {average:.1f}!",
                color="cyan",
            )
        )
    elif 7 > average >= 5:
        print(
            cs.colorize(
                f"Aluno(a) DE RECUPERAÇÃO com média {average:.1f}!",
                color="yellow",
            )
        )
    else:
        print(
            cs.colorize(
                f"Aluno(a) REPROVADO(A) com média {average:.1f}!",
                color="lilac",
            )
        )


if __name__ == "__main__":
    run()
