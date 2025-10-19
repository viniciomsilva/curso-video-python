# 004
# FAÇA UM PROGRAMA QUE LEIA ALGO DO TECLADO E MOSTRE NA TELA O SEU TIPO
# PRIMITIVO E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE

from scripts.custom import customize


def istrue(condition):
    return (
        "{}".format(
            customize(
                " SIM ",
                back="cyan",
            )
        )
        if condition
        else "{}".format(
            customize(
                " NÃO ",
                back="magenta",
            )
        )
    )


def run():
    anything = input("Digite alguma coisa: ")

    print("É espaço?       {}".format(istrue(anything.isspace())))
    print("É minúsculo?    {}".format(istrue(anything.islower())))
    print("É maiúsculo?    {}".format(istrue(anything.isupper())))
    print("É capitalizado? {}".format(istrue(anything.istitle())))
    print("É alfanumérico? {}".format(istrue(anything.isalpha())))
    print("É só numérico?  {}".format(istrue(anything.isnumeric())))
    print("É decimal?      {}".format(istrue(anything.isdecimal())))
