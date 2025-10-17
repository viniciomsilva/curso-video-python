# 039
# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO
# COM SUA IDADE:
# 	- SE ELE AINDA VAI SE ALISTA AO SERVIÇO MILITAR
# 	- SE ESTÁ NA HORA DE SE ALISTA AO SERVIÇO MILITAR
# 	- SE JÁ PASSOU DO TEMPO DE SE ALISTAR AO SERVIÇO MILITAR
# O PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO

from datetime import date

from utils import custom as cs


def run():
    year_birth = int(input("Digite o ano de nascimento: "))

    this_year = date.today().year
    age = this_year - year_birth

    if year_birth > this_year:
        print(cs.colorize("Ops! Ano de nascimento inválido.", "red"))
    else:
        print("Ele tem {} anos. ".format(age), end="")
        if age < 18:
            print(
                cs.colorize(
                    f"Faltam {(18 - age)} anos para o alistamento militar.",
                    color="green",
                ),
            )
        elif age > 18:
            print(
                cs.colorize(
                    f"Passaram {(age - 18)} anos do alistamento militar.",
                    color="lilac",
                ),
            )
        else:
            print(
                cs.colorize(
                    "Está na data para o alistamento militar.",
                    color="cyan",
                )
            )


if __name__ == "__main__":
    run()
