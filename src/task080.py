# 080
# Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os numa lista, já na posição correta de inserção
# (sem usar o sorted()). No final, mostre a lista ordenada na tela.


def run():
    length = 0
    current = 0
    values = []

    for _ in range(5):
        value = int(input("Digite um valor: ").strip())

        current = 0 if length == 0 else length

        for i, v in enumerate(values):
            if value <= v:
                current = i
                break

        values.insert(current, value)
        length = len(values)

    print(f"Os valores digitados foram: {values}")


if __name__ == "__main__":
    run()
