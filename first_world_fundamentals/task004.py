# 004
# FAÇA UM PROGRAMA QUE LEIA ALGO DO TECLADO E MOSTRE NA TELA O SEU TIPO
# PRIMITIVO E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE

from custom import clear
from custom import customize


def istrue(condition):
    return (
        f"{customize(style="bold", back="cyan")} SIM {clear()}"
        if condition
        else f"{customize(style="bold", back="lilac")} NÃO {clear()}"
    )


if __name__ == "__main__":
    anything = input("DIGITE ALGUMA COISA.: ")

    print(f"É ESPAÇO?       {istrue(anything.isspace())}")
    print(f"É MINÚSCULO?    {istrue(anything.islower())}")
    print(f"É MAIÚSCULO?    {istrue(anything.isupper())}")
    print(f"É CAPITALIZADO? {istrue(anything.istitle())}")
    print(f"É ALFANUMÉRICO? {istrue(anything.isalpha())}")
    print(f"É NUMÉRICO?     {istrue(anything.isnumeric())}")
    print(f"É DECIMAL?      {istrue(anything.isdecimal())}")
