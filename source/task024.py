# 024
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO
# COM A PALAVRA "SANTO"

from utils import custom as cs


def run():
    holy = ["são", "santo", "santa", "santos", "santas"]

    city_name = input("DIGITE O NOME DA SUA CIDADE: ").strip().lower()
    first_city_name = city_name.split()[0]

    if city_name in holy or first_city_name in holy:
        print(
            cs.colorize(
                f"A cidade {city_name.title()} é santa!",
                color="cyan",
            )
        )
    else:
        print(
            cs.colorize(
                f"A cidade {city_name.title()} NÃO é santa!",
                color="lilac",
            )
        )


if __name__ == "__main__":
    run()
