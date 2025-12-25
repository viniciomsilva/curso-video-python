# 084
# Faça um programa que leia o nome peso de várias pessoas, guardando tudo numa
# lista. No final, mostre:
#   - Quantas pessoas foram cadastradas
#   - Uma listagem com as pessoas mais pesadas
#   - Uma listagem com as pessoas mais leves

from cli.io import inputf_flo
from cli.io import leave


def __name_people_weight(
    p: list[dict[str, str | float]],
    w: float,
) -> list[str]:
    return [str(y["name"]) for y in filter(lambda x: x["weight"] == w, p)]


if __name__ == "__main__":
    people: list[dict[str, str | float]] = []
    fatter = 0
    tinner = 0

    while True:
        name = input("Nome: ").strip().title()
        weight = inputf_flo("Peso (KG): ")

        if weight > fatter:
            fatter = weight
        if weight < tinner or tinner == 0:
            tinner = weight

        people.append({"name": name, "weight": weight})

        if leave("Cadastrar outra? [s/n] "):
            break

    print(f"\nQuantidade de pessoas: {len(people)}")
    print(
        "Maior peso: {}kg. As pessoas com ele são: {}".format(
            fatter,
            ", ".join(__name_people_weight(people, fatter)),
        )
    )
    print(
        "Menor peso: {}kg. As pessoas com ele são: {}".format(
            tinner,
            ", ".join(__name_people_weight(people, tinner)),
        )
    )
