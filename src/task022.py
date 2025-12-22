# 022
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E MOSTRE:
#   O NOME COM TODAS AS LETRAS MAIÚSCULAS
#   O NOME COM TODAS AS LETRAS MINÚSCULAS
#   QUANTAS LETRAS TOTAIS (SEM CONSIDERAR OS ESPAÇO)
#   QUANTAS LETRAS TEM O PRIMEIRO NOME


def run():
    name = str(input("Digite o seu nome completo: ")).strip()

    print(
        "\nSeu nome em letras maiúsculas: {}".format(
            name.upper(),
        )
    )
    print(
        "Seu nome em letras minúsculas: {}".format(
            name.lower(),
        )
    )
    print(
        "Quantidade de letras no seu nome: {}".format(
            len(name.replace(" ", "")),
        )
    )
    print(
        "Quantidade de letras no seu primeiro nome: {}".format(
            len(name.split()[0]),
        )
    )


if __name__ == "__main__":
    run()
