# 026
# CRIE UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
#   QUANTAS VEZES APARECEM A LETRA 'A'
#   EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
#   EM QUE POSIÇÃO ELA APARECE A ULTIMA VEZ

from scripts.custom import customize


def run():
    phrase = input("Digite uma frase qualquer: ").strip().lower()

    first = phrase.find("a")
    last = phrase.rfind("a")

    print(
        "\nQuantidade de 'A': {}".format(
            customize(
                " {:5} ".format(phrase.count("a")),
                style="bold",
                back="yellow",
            )
        )
    )
    print(
        "Primeiro 'A'.....: {}".format(
            customize(
                " {:5} ".format(
                    first + 1 if first >= 0 else "NaN",
                ),
                style="bold",
                back="cyan",
            )
        )
    )
    print(
        "Último 'A'.......: {}".format(
            customize(
                " {:5} ".format(
                    last + 1 if last >= 0 else "NaN",
                ),
                style="bold",
                back="cyan",
            )
        )
    )


if __name__ == "__main__":
    run()
