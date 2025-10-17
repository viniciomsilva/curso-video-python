# 022
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E MOSTRE:
#   O NOME COM TODAS AS LETRAS MAIÚSCULAS
#   O NOME COM TODAS AS LETRAS MINÚSCULAS
#   QUANTAS LETRAS TOTAIS (SEM CONSIDERAR OS ESPAÇO)
#   QUANTAS LETRAS TEM O PRIMEIRO NOME


def run():
    name = str(input("Digite o seu nome completo: ")).strip()

    print(f"\nSeu nome em letras maiúsculas: {name.upper()}")
    print(f"Seu nome em letras minúsculas: {name.lower()}")
    print(f"Quantidade de letras no seu nome: {len(name.replace(" ", ""))}")
    print(f"Quantidade de letras no seu primeiro nome: {len(name.split()[0])}")


if __name__ == "__main__":
    run()
