# 080
# Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os numa lista, já na posição correta de inserção
# (sem usar o sorted()). No final, mostre a lista ordenada na tela.

from cli.io import inputf_int


if __name__ == "__main__":
    length = 0
    current = 0
    values: list[int] = []

    for _ in range(5):
        value = inputf_int("Digite um valor: ")

        current = 0 if length == 0 else length

        for i, v in enumerate(values):
            if value <= v:
                current = i
                break

        values.insert(current, value)
        length = len(values)

    print(
        "Os valores digitados foram: {}".format(
            ", ".join(map(str, values)),
        )
    )
