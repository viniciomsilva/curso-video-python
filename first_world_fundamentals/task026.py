# 026
# CRIE UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
#   QUANTAS VEZES APARECEM A LETRA 'A'
#   EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
#   EM QUE POSIÇÃO ELA APARECE A ULTIMA VEZ

from custom import clear
from custom import customize


if __name__ == "__main__":
    phrase = input("DIGITE UMA FRASE QUALQUER: ").lower().strip()

    first = phrase.find("a")
    last = phrase.rfind("a")

    print(
        "QUANTIDADE DE 'A': {} {:5} {}".format(
            customize(style="bold", back="yellow"),
            phrase.count("a"),
            clear(),
        )
    )
    print(
        "PRIMERO 'A'......: {} {:5} {}".format(
            customize(style="bold", back="cyan"),
            first + 1 if (first >= 0) else "NaN",
            clear(),
        )
    )
    print(
        "ULTIMO 'A'.......: {} {:5} {}".format(
            customize(style="bold", back="lilac"),
            last + 1 if (last >= 0) else "NaN",
            clear(),
        )
    )
