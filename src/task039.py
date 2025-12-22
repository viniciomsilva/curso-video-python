# 039
# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO
# COM SUA IDADE:
# 	- SE ELE AINDA VAI SE ALISTA AO SERVIÇO MILITAR
# 	- SE ESTÁ NA HORA DE SE ALISTA AO SERVIÇO MILITAR
# 	- SE JÁ PASSOU DO TEMPO DE SE ALISTAR AO SERVIÇO MILITAR
# O PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO

from datetime import date

from cli.io import printf


def run():
    year_birth = int(input("Digite o ano de nascimento: "))

    this_year = date.today().year
    age = this_year - year_birth

    if year_birth > this_year:
        printf(
            "Ops! Ano de nascimento inválido.",
            style="bold",
            color="magenta",
        )
    else:
        printf(
            "Ele tem {} anos. ".format(age),
            start="\n",
            end="",
            style="bold",
        )
        if age < 18:
            printf(
                "Faltam {} anos para o alistamento militar.".format(18 - age),
                style="bold",
                color="green",
            )
        elif age > 18:
            printf(
                "Passaram {} anos do alistamento militar.".format(age - 18),
                style="bold",
                color="magenta",
            )
        else:
            printf(
                "Está na data de se alistar.",
                style="bold",
                color="cyan",
            )


if __name__ == "__main__":
    run()
