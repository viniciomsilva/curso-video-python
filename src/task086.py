# 086
# Crie um programa que crie uma matriz de dimensão 3x3 e preencha-a com valores
# lidos pelo teclado. No final, mostre-a na tela com a formatação correta.

# 087
# Aprimore o desafio anterior, mostrando:
#   - A soma de todos os valores pares digitados
#   - A soma dos valores da terceira coluna
#   - O maior valor da segunda linha

from cli.io import inputf_int


if __name__ == "__main__":
    values: list[int] = []
    matrix: list[list[int]] = []
    sum_even = 0

    for i in range(9):
        n = inputf_int(f"{i + 1}o. valor: ")

        if n % 2 == 0:
            sum_even += n

        values.append(n)

    matrix = [values[i : i + 3] for i in range(0, 9, 3)]

    print()
    print("-" * 23)

    for x in range(3):
        for y in range(3):
            print(f"|{matrix[x][y]:^5}|", end=" ")
        print()

    print("-" * 23)

    print(f"\nSoma de todos os pares: {sum_even}")
    print(f"O maior valor da segunda linha: {max(matrix[1])}")
    print(
        "Soma de todos da terceira coluna: {}".format(
            sum([matrix[i][2] for i in range(3)]),
        )
    )
