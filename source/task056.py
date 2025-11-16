# 056
# Desenvolva um programa que leia nome, idade e sexo de quatro pessoas. No final
# mostre:
#   - A média de idade do grupo
#   - Qual é o nome do homem mais velho
#   - Quantas mulheres têm menos de vinte anos

# 069
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
# cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No
# final, mostre:
#   - Quantas pessoas têm mais de 18 anos
#   - Quantos homens foram cadastrados
#   - Quantas mulheres têm menos de 20 anos

from statistics import mean

from classes.person import Person
from cli.io import EXIT_CMDS
from cli.io import printf
from cli.io import inputf
from cli.wait import wait


def __age(person: Person) -> int:
    return person.age


def __sex(people: list[Person], sex: str) -> list[Person]:
    return list(filter(lambda x: x.info["sex"] in sex, people))


def __older_man(people: list[Person]) -> tuple:
    men = __sex(people, "masc")

    if not men:
        return None, 0

    return sorted(men, key=__age, reverse=True)[0], len(men)


def __adults(people: list[Person]) -> int:
    adults = list(filter(lambda x: x.age > 18, people))

    return len(adults)


def __young_women(people: list[Person]) -> list[Person] | None:
    women = __sex(people, "fem")

    if not women:
        return None

    return list(filter(lambda x: x.age < 20, women))


def run():
    rps = ""
    people: list[Person] = []

    while True:
        printf("Nova pessoa: ", start="\n", style="bold")

        name = input("Nome: ").title().strip()
        birth = input("Ano de nascimento: ")
        sex = input("Sexo: [M] Masc [F] Fem: ").lower().strip()

        people.append(Person(name, int(birth), sex))

        if (
            inputf(
                "Cadastrar outra pessoa? [S/N] ",
                style="bold",
                color="yellow",
            )
            in EXIT_CMDS
        ):
            break

    older_man, number_of_men = __older_man(people)
    young_women = __young_women(people)
    rps = "Média de idade: {:.1f} anos!".format(
        mean([person.age for person in people]),
    )
    rps += "\nQuantidade de adultos: {}".format(__adults(people))

    if older_man:
        rps += "\nQuantidade homens: {}".format(number_of_men)
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
