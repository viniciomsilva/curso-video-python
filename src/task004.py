# 004
# Faça um programa que leia algo do teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveis sobre ele.

from cli.ux import customize


def __is_true(condition: bool) -> str:
    return (
        f"{customize(" SIM ", back="cyan")}"
        if condition
        else f"{customize(" NÃO ", back="magenta")}"
    )


if __name__ == "__main__":
    anything = input("Digite alguma coisa: ")

    print(f"É espaço?       {__is_true(anything.isspace())}")
    print(f"É minúsculo?    {__is_true(anything.islower())}")
    print(f"É maiúsculo?    {__is_true(anything.isupper())}")
    print(f"É capitalizado? {__is_true(anything.istitle())}")
    print(f"É alfanumérico? {__is_true(anything.isalpha())}")
    print(f"É só numérico?  {__is_true(anything.isnumeric())}")
    print(f"É decimal?      {__is_true(anything.isdecimal())}")
