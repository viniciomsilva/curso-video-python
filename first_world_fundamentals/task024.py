# 024
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO
# COM A PALAVRA "SANTO"

holy = ["SÃO", "SANTO", "SANTA", "SANTOS", "SANTAS"]

if __name__ == "__main__":
    name_city = input("DIGITE O NOME DA SUA CIDADE: ").upper()
    first_name_city = name_city.split()[0]

    if name_city in holy or first_name_city in holy:
        print(f"\nA CIDADE {name_city} É SANTA!")
    else:
        print(f"\nA CIDADE {name_city} NÃO É SANTA!")
