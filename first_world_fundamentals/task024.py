# 024
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO
# COM A PALAVRA "SANTO"

from custom import customize


if __name__ == "__main__":
    holy = ["SÃO", "SANTO", "SANTA", "SANTOS", "SANTAS"]

    city_name = input("DIGITE O NOME DA SUA CIDADE: ").upper().strip()
    first_city_name = city_name.split()[0]

    if city_name in holy or first_city_name in holy:
        print(
            "\n{}A CIDADE {} É SANTA!".format(
                customize(style="bold", color="cyan"), city_name
            )
        )
    else:
        print(
            "\n{}A CIDADE {} NÃO É SANTA!".format(
                customize(style="bold", color="lilac"), city_name
            )
        )
