# 024
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO
# COM A PALAVRA "SANTO"

from scripts.custom import customize


def run():
    holy = ["são", "santo", "santa", "santos", "santas"]

    city_name = input("Digite o nome da sua cidade: ").strip().lower()
    first_city_name = city_name.split()[0]

    if city_name in holy or first_city_name in holy:
        print(
            customize(
                "A cidade {} é santa!".format(
                    city_name.title(),
                ),
                style="bold",
                color="cyan",
            )
        )
    else:
        print(
            customize(
                "A cidade {} NÃO é santa!".format(
                    city_name.title(),
                ),
                style="bold",
                color="magenta",
            )
        )
