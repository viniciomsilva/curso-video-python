# 100
# Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 valores
# e vai colocá-los dentro da lista. A segunda função vai mostrar a soma de
# todos os valores pares sorteados pela função anterior.

from random import randint


def __draw_numbers(limit: int = 5) -> list[int]:
    if limit <= 0:
        limit = 5

    return [randint(0, 100) for _ in range(limit)]


def __even_odd(values: list[int], iseven: bool = True) -> tuple[list[int], int]:
    n = []

    if iseven:
        n = list(filter(lambda x: x % 2 == 0, values))
    else:
        n = list(filter(lambda x: x % 2 != 0, values))

    return n, sum(n[:])


if __name__ == "__main__":
    limit = int(input("Quantidade de valores a serem sorteados: ").strip())

    values = __draw_numbers(limit)
    even, se = __even_odd(values)
    odd, so = __even_odd(values, False)

    print("\nValores sorteados: {}".format(values))
    print("O valores pares são: {}. E somam: {}".format(even, se))
    print("O valores ímpares são: {}. E somam: {}".format(odd, so))
