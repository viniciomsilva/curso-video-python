# 041
# A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE
# NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE:
# 	- ATÉ 9 ANOS:	MIRIM
# 	- ATÉ 14 ANOS:	INFANTIL
# 	- ATÉ 19 ANOS:	JÚNIOR
# 	- ATÉ 20 ANOS:  SÊNIOR
# 	- ACIMA:	    MASTER

from datetime import date

from cli.io import printf


def run():
    rps = {
        "content": "",
        "back": "",
    }
    birth = int(input("Data de nascimento: "))

    age = date.today().year - birth

    rps["content"] = " Ele(a) tem {} anos. ".format(age)
    if age <= 9:
        rps["content"] += "Categoria MIRIM. "
        rps["back"] = "green"
    elif age <= 14:
        rps["content"] += "Categoria INFANTIL. "
        rps["back"] = "blue"
    elif age <= 19:
        rps["content"] += "Categoria JÚNIOR. "
        rps["back"] = "yellow"
    elif age <= 25:
        rps["content"] += "Categoria SÊNIOR. "
        rps["back"] = "magenta"
    else:
        rps["content"] += "Categoria MASTER. "
        rps["back"] = "cyan"

    printf(
        rps["content"],
        start="\n",
        style="bold",
        back=rps["back"],
    )
