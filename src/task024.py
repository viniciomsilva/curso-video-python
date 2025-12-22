# 024
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO
# COM A PALAVRA "SANTO"

from cli.io import printf


def run():
    holy = ["são", "santo", "santa", "santos", "santas"]

    city_name = input("Digite o nome da sua cidade: ").strip().lower()
    first_city_name = city_name.split()[0]

    if city_name in holy or first_city_name in holy:
        printf(
            "A cidade {} é santa!".format(city_name.title()),
            start="\n",
            style="bold",
            color="cyan",
        )
    else:
        printf(
            "A cidade {} NÃO é santa!".format(city_name.title()),
            start="\n",
            style="bold",
            color="magenta",
        )


if __name__ == "__main__":
    run()
