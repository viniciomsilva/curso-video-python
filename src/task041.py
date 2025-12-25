# 041
# A Confederação Nacional de Natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#   - Até 9 anos (mirim);
#   - Até 14 anos (infantil);
#   - Até 19 anos (júnior);
#   - Até 20 anos (sênior);
#   - Acima (master).

from cli.io import inputf_int
from cli.io import printf
from cli.ux import THIS_YEAR


if __name__ == "__main__":
    rps = {
        "content": "",
        "back": "",
    }

    birth = inputf_int("Ano de nascimento: ")
    age = THIS_YEAR - birth

    rps["content"] = f" Ele(a) tem {age} anos. "

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
