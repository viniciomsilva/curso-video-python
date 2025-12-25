# 026
# Crie um programa que leia uma frase pelo teclado e mostre:
#   - Quantas vezes aparecem a letra 'A';
#   - Em que posição ela aparece a primeira vez;
#   - Em que posição ela aparece a ultima vez.

from cli.ux import customize


if __name__ == "__main__":
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
