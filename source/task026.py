# 026
# CRIE UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
#   QUANTAS VEZES APARECEM A LETRA 'A'
#   EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
#   EM QUE POSIÇÃO ELA APARECE A ULTIMA VEZ

from utils import custom as cs


def run():
    phrase = input("Digite uma frase qualquer: ").strip().lower()

    first = phrase.find("a")
    last = phrase.rfind("a")

    print(
        "Quantidade de 'A': {}".format(
            cs.colorize(
                f" {phrase.count("a"):5} ",
                back="yellow",
            )
        )
    )
    print(
        "Primeiro 'A'......: {} {:5} {}".format(
            cs.customize(style="bold", back="cyan"),
            first + 1 if (first >= 0) else "NaN",
            cs.clean(),
        )
    )
    print(
        "Último 'A'.......: {} {:5} {}".format(
            cs.customize(style="bold", back="lilac"),
            last + 1 if (last >= 0) else "NaN",
            cs.clean(),
        )
    )


if __name__ == "__main__":
    run()
