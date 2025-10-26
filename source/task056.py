# 056
# Desenvolva um programa que leia nome, idade e sexo de quatro pessoas. No final
# mostre:
#   - A média de idade do grupo
#   - Qual é o nome do homem mais velho
#   - Quantas mulheres têm menos de vinte anos

from classes.person import Person
from cli.io import inputf
from cli.io import printf
from cli.wait import wait


def __avg(x: list) -> float:
    return sum(x) / len(x)


def __age(person: Person) -> int:
    return person.age


def __sex(people: list[Person], sex: str) -> list[Person]:
    return list(filter(lambda x: x.info["sex"] in sex, people))


def __older_man(people: list[Person]) -> Person | None:
    men = __sex(people, "masc")

    if not men:
        return None

    return sorted(men, key=__age, reverse=True)[0]


def __young_women(people: list[Person]) -> list[Person] | None:
    women = __sex(people, "fem")

    if not women:
        return None

    return list(filter(lambda x: x.age < 20, women))


def run():
    rps = ""
    people: list[Person] = []

    qnt = int(input("Quantidade de pessoas: "))
    for i in range(qnt):
        printf("Dados da {}ª pessoa: ".format(i + 1), start="\n", style="bold")

        name = input("Nome: ").title().strip()
        birth = input("Ano de nascimento: ")
        sex = input("Sexo: [M] Masc [F] Fem: ").lower().strip()

        people.append(Person(name, int(birth), sex))

    older_man = __older_man(people)
    young_women = __young_women(people)
    rps = "Média de idade: {:.1f} anos!".format(
        __avg([person.age for person in people]),
    )

    if older_man:
        rps += "\n{} é o homem mais velho com {} anos!".format(
            older_man.info["name"],
            older_man.info["age"],
        )
    else:
        rps += "\nNão há homens!!!"

    if young_women:
        rps += "\nHá {} mulheres com MENOS de 20 anos!".format(len(young_women))
    else:
        rps += "\nNão há mulheres com MENOS de 20 anos!!!"

    wait("Analisando...")
    printf(rps, style="bold")
