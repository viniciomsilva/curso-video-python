# 004
# FAÇA UM PROGRAMA QUE LEIA ALGO DO TECLADO E MOSTRE NA TELA O SEU TIPO
# PRIMITIVO E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE

from utils import custom as cs


def istrue(condition):
    return (
        f"{cs.colorize(" SIM ", back="cyan")}"
        if condition
        else f"{cs.colorize(" NÃO ", back="lilac")}"
    )


def run():
    anything = input("Digite alguma coisa.: ")

    print(f"É espaço?       {istrue(anything.isspace())}")
    print(f"É minúsculo?    {istrue(anything.islower())}")
    print(f"É maiúsculo?    {istrue(anything.isupper())}")
    print(f"É capitalizado? {istrue(anything.istitle())}")
    print(f"É alfanumérico? {istrue(anything.isalpha())}")
    print(f"É só numérico?  {istrue(anything.isnumeric())}")
    print(f"É decimal?      {istrue(anything.isdecimal())}")


if __name__ == "__main__":
    run()
