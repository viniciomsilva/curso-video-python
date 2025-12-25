# 092
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# de uma pessoa e cadastre-os (com idade) num dicionário. Se a CTPS for
# diferente de ZERO, o dicionário receberá também o ano de contratação e
# o salário. Calcule e acrescente, além da idade, com quando anos a pessoa
# vai se aposentar.

from cli.io import inputf_flo
from cli.io import inputf_int
from cli.ux import THIS_YEAR


if __name__ == "__main__":
    name = input("Nome: ").strip().title()
    birth = inputf_int("Ano de nascimento: ")

    age = THIS_YEAR - birth
    person: dict[str, str | int | float] = {"name": name, "age": age}

    if age >= 18:
        ctps = inputf_int("N.º CTPS: ")

        if ctps != 0:
            person["ctps"] = ctps
            person["year_hiring"] = inputf_int("Ano de contratação: ")
            person["salary"] = inputf_flo("Salário: R$ ")
            person["retirement"] = age + 35 - (THIS_YEAR - person["year_hiring"])

    print("-" * 30)
    for k, v in person.items():
        print(f"  > Chave '{k}' tem valor: {v}")
