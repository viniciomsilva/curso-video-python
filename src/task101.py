# 101
# Crie um programa que tenha uma função chamada voto() que vai receber como
# parâmetro o ano de nascimento de uma pessoa, retornando uma valor literal
# indicando se ela tem voto NEGADO, OBRIGATÓRIO ou OPCIONAL nas eleições.

from datetime import date

from cli.io import printf


def __vote(birth: int) -> str:
    age = date.today().year - birth

    if age < 16:
        return f"Com {age} anos o voto é NEGADO!"
    elif age < 18 or age >= 70:
        return f"Com {age} anos, o voto é FACULTATIVO!"

    return f"Com {age} anos, o voto é OBRIGATÓRIO!"


def run():
    birth = int(input("Ano de nascimento: "))

    printf(__vote(birth), style="bold")


if __name__ == "__main__":
    run()
