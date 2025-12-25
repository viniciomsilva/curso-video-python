# 089
# Crie um programa que leia o nome e duas notas de vários aluno e guarde tudo
# numa lista composta. No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa ver as notas de cada aluno individualmente.

from statistics import mean

from cli.io import __EXIT_CMDS


def run():
    students = []

    while True:
        notes = []
        name = input("\nNome do(a) aluno(a): ").strip().title()

        for i in range(2):
            note = float(input(f"{i + 1}º nota: "))
            notes.append(note)

        students.append({"name": name, "notes": notes})

        if input("Quer continuar? [s/n] ") in __EXIT_CMDS:
            break

    print(f"\nNo | Aluno(a) {' ':11} Média")
    for i, s in enumerate(students):
        print(
            "{:2} | {:20} {:>6.1f}".format(
                i,
                s["name"],
                mean(s["notes"]),
            )
        )

    while True:
        op = int(input("\nVer notas individuais? [-1 finaliza] "))

        if not op < 0:
            print(
                "A notas de {} foram: {}".format(
                    students[op]["name"],
                    ", ".join(map(str, students[op]["notes"])),
                )
            )
        else:
            break


if __name__ == "__main__":
    run()
