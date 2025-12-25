# 024
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
# com a palavra "santo".

from cli.io import printf


if __name__ == "__main__":
    holy = ("são", "santo", "santa", "santos", "santas")

    city_name = input("Digite o nome da sua cidade: ").strip().lower()
    first_city_name = city_name.split(" ")[0]

    if city_name in holy or first_city_name in holy:
        printf(
            f"A cidade {city_name.title()} é santa!",
            start="\n",
            style="bold",
            color="cyan",
        )
    else:
        printf(
            f"A cidade {city_name.title()} NÃO é santa!",
            start="\n",
            style="bold",
            color="magenta",
        )
