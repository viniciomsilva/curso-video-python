# 039
# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO
# COM SUA IDADE:
# 	- SE ELE AINDA VAI SE ALISTA AO SERVIÇO MILITAR
# 	- SE ESTÁ NA HORA DE SE ALISTA AO SERVIÇO MILITAR
# 	- SE JÁ PASSOU DO TEMPO DE SE ALISTAR AO SERVIÇO MILITAR
# O PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO

from datetime import date

from scripts.custom import customize


def run():
    year_birth = int(input("Digite o ano de nascimento: "))

    this_year = date.today().year
    age = this_year - year_birth

    if year_birth > this_year:
        print(
            customize(
                "Ops! Ano de nascimento inválido.",
                style="bold",
                color="magenta",
            )
        )
    else:
        print("Ele tem {} anos. ".format(age), end="")
        if age < 18:
            print(
                customize(
                    "Faltam {} anos para o alistamento militar.".format(
                        18 - age,
                    ),
                    style="bold",
                    color="green",
                ),
            )
        elif age > 18:
            print(
                customize(
                    "Passaram {} anos do alistamento militar.".format(
                        age - 18,
                    ),
                    style="bold",
                    color="magenta",
                ),
            )
        else:
            print(
                customize(
                    "Está na data para o alistamento militar.",
                    style="bold",
                    color="cyan",
                )
            )
