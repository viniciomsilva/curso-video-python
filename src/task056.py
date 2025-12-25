# 056, 069 e 094
# Crie um programa que leia: nome, idade e sexo de várias pessoas.
# No final, mostre as seguintes análises:

#   - Quantas pessoas foram cadastradas
#   - A média de idade do grupo
#   - Quantas pessoas têm mais de 18 anos
#   - Uma lista com todas as pessoas com idade acima da média
#   - Quantos homens foram cadastrados
#   - Qual é o nome do homem mais velho
#   - Uma lista com todas as mulheres
#   - Quantas mulheres têm menos de 20 anos

from statistics import mean

from classes.person import Person
from cli.io import inputf_int
from cli.io import printf
from cli.io import leave
from cli.ux import THIS_YEAR
from cli.ux import wait
from cli.ux import clear


def __age(person: Person) -> int:
    return person.age


def __filter_age(
    people: list[Person],
    age: float,
    greater: bool = True,
) -> list[Person]:
    if greater:
        return list(filter(lambda p: p.age > age, people))
    return list(filter(lambda p: p.age < age, people))


def __filter_sex(
    people: list[Person],
    sex: str,
) -> list[Person]:
    return list(filter(lambda x: str(x.info["sex"]) in sex, people))


def __analyse(people: list[Person]) -> list[str]:
    analysis: list[str] = []

    men = __filter_sex(people, "m")
    women = __filter_sex(people, "f")
    age_mean = mean([p.age for p in people])
    adults = __filter_age(people, 18)
    people_above_mean_age = __filter_age(people, age_mean)

    analysis.append("- Quantidade de pessoas: {}".format(len(people)))
    analysis.append("- Quantidade de adultos: {}".format(len(adults)))
    analysis.append("- Média de idade do grupo: {}".format(age_mean))
    analysis.append(
        "- Pessoas com idade acima da média: {}".format(
            [(p.info["name"], p.age) for p in people_above_mean_age]
        )
    )

    if men:
        old_man = sorted(men, key=__age, reverse=True)[0]

        analysis.append("- Quantidade de homens: {}".format(len(men)))
        analysis.append(
            "  - O homem mais velho é {} com {} anos!".format(
                old_man.info["name"],
                old_man.age,
            )
        )
    else:
        analysis.append("- Não há homens!")

    if women:
        young_women = __filter_age(women, 20, greater=False)

        analysis.append(
            "- Todas as mulheres: {}".format(
                [w.info["name"] for w in women],
            )
        )
        analysis.append(
            "  - Quantidade de mulheres jovens: {}".format(
                len(young_women),
            )
        )
    else:
        analysis.append("- Não há mulheres!")

    return analysis


if __name__ == "__main__":
    people: list[Person] = []
    wait_times = (
        ("Iniciando análise...", 1),
        ("Analisando...", 3),
        ("Terminando a análise...", 1),
    )

    # input
    while True:
        printf("Nova pessoa: ", style="bold")

        name = input("Nome: ").title().strip()

        while True:
            birth = inputf_int("Ano de nascimento: ")

            if birth <= THIS_YEAR:
                break

        while True:
            sex = input("Sexo: [M] Masc [F] Fem: ").lower().strip()[0]

            if sex in "fm":
                break

            printf("Por favor, tente novamente! ", color="magenta")

        people.append(Person(name, birth, sex))

        if leave(
            "Cadastrar outra pessoa? [y/n] ",
            style="bold",
            color="yellow",
        ):
            break

        clear()

    # analysis
    analysis = __analyse(people)

    # output
    for wt in wait_times:
        wait(wt[0], time=wt[1], end="")

    clear()
    printf("Análise concluída...", end="\n\n", style="bold", color="cyan")

    for data in analysis:
        printf(data, style="bold")

    print()
