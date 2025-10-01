# 023
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO ENTRE 0 E 9999 E MOSTRE CADA UM DOS
# DÍGITOS SEPARADOS

def divide(dividend: int, divisor: int) -> tuple[int, int]:
    return (dividend // divisor), (dividend % divisor)


if __name__ == "__main__":
    num = input("DIGITE UM NÚMERO ENTRE 0 E 9999: ").rjust(4, "0")

    print("\nCOM MANIPULAÇÃO DE TEXTO")
    print(f"MILHAR................: {num[0]}")
    print(f"CENTENA...............: {num[1]}")
    print(f"DEZENA................: {num[2]}")
    print(f"UNIDADE...............: {num[3]}")

    num = int(num)

    m, rest = divide(num, 1000)
    c, rest = divide(rest, 100)
    d, rest = divide(rest, 10)

    print("\nCOM MANIPULAÇÃO NUMÉRICA")
    print(f"MILHAR................: {m}")
    print(f"CENTENA...............: {c}")
    print(f"DEZENA................: {d}")
    print(f"UNIDADE...............: {rest}")
