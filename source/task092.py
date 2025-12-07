# 092
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# de uma pessoa e cadastre-os (com idade) num dicionário. Se a CTPS for
# diferente de ZERO, o dicionário receberá também o ano de contratação e
# o salário. Calcule e acrescente, além da idade, com quando anos a pessoa
# vai se aposentar.

from datetime import date

from classes.person import Person


def run():
    year = date.today().year

    name = input("Nome: ").strip().title()
    birth = int(input("Ano de nascimento: "))

    person = Person(name, birth).info
    del person["sex"]

    if person["age"] >= 18:
        ctps = int(input("N.º CTPS: "))

        if ctps != 0:
            person["ctps"] = ctps
            person["year_hiring"] = int(input("Ano de contratação: "))
            person["salary"] = float(input("Salário: R$ "))
            person["retirement"] = person["age"] + 35 - (year - person["year_hiring"])

    print("-" * 30)
    for k, v in person.items():
        print(f"  > Chave '{k}' tem valor: {v}")
