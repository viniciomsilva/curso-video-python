# 039
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
# com sua idade:
#   - Se ele ainda vai se alista ao serviço militar;
#   - Se está na hora de se alista ao serviço militar;
#   - Se já passou do tempo de se alistar ao serviço militar.
# O programa também deverá mostrar o tempo que falta ou que passou do prazo.

from cli.io import inputf_int
from cli.io import printf
from cli.ux import THIS_YEAR


if __name__ == "__main__":
    birth = inputf_int("Digite o ano de nascimento: ")

    age = THIS_YEAR - birth

    if birth > THIS_YEAR:
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
