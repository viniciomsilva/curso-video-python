# 023
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO ENTRE 0 E 9999 E MOSTRE CADA UM DOS
# DÍGITOS SEPARADOS


decimal_orders = [
    "UNIDADE", "DEZENA", "CENTENA",
    "UNIDADE DE MILHAR", "DEZENA DE MILHAR", "CENTENA DE MILHAR"
]


def print_separate_numbers(num):
    length = len(num)
    num = int(num)
    divisor = 1

    print()
    for i in range(length):
        print(f"{decimal_orders[i]}: {num // divisor % 10}")

        divisor *= 10


if __name__ == "__main__":
    num = input("DIGITE UM NÚMERO ENTRE 0 E 999999: ").strip()

    print_separate_numbers(num=num)
