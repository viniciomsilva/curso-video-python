# 077
# Crie um programa que tenha uma tupla com várias palavras (não utilizar
# acentos). Depois disso, você deve mostrar, para cada palavra, quais são as
# suas vogais.


def run():
    words = (
        "aprender",
        "programar",
        "linguagem",
        "python",
        "curso",
        "gratis",
        "estudar",
        "praticar",
        "trabalhar",
        "mercado",
        "programador",
        "futuro",
    )

    for word in words:
        vowels = set(filter(lambda x: x.lower() in "aeiou", word))

        print(
            "Na palavra {} há as vogais: {}".format(
                word.upper(),
                ", ".join(vowels),
            )
        )
