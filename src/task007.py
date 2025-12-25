# 007
# Desenvolva um programa que leia duas notas de um aluno, calcule e
# mostre a sua média.

# 040
# crie um programa que leia duas notas de um aluno, calcule a média e
# mostre a situação dele de acordo com ela:
#   - Abaixo de 5.0:    Reprovado
#   - Entre 5.0 e 6.9:  Recuperação
#   - Acima de 7.0:     Aprovado

# 090
# Faça um programa que leia nome e média de um aluno, guardando também a
# situação. No final, mostre o conteúdo da estrutura na tela.

from statistics import mean

from cli.io import printf
from cli.io import inputf_flo
from cli.ux import wait


if __name__ == "__main__":
    msg = {"content": "", "color": ""}
    student = {"name": "", "grades": [0, 0], "avg": 0}  # type: ignore

    student["name"] = input("Nome do(a) aluno(a): ").strip().title()

    for i in range(2):
        student["grades"][i] = inputf_flo(
            "{}ª nota de {}: ".format(
                i + 1,
                student["name"],
            )
        )

    wait("Calculando...")

    student["avg"] = mean(student["grades"])  # type: ignore
    msg["content"] = f"com média {student['avg']:.1f}!"

    if student["avg"] >= 7:
        msg["content"] = f"{student['name']} APROVADO(A) {msg['content']}"
        msg["color"] = "cyan"
    elif 5 <= student["avg"] < 7:
        msg["content"] = f"{student['name']} DE RECUPERAÇÃO {msg['content']}"
        msg["color"] = "yellow"
    else:
        msg["content"] = f"{student['name']} REPROVADO {msg['content']}"
        msg["color"] = "magenta"

    printf(
        msg["content"],
        style="bold",
        color=msg["color"],
    )
