# 033
# FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL O MENOR.

if __name__ == "__main__":
    # num1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
    # num2 = int(input("DIGITE O SEGUNDO NÚMERO.: "))
    # num3 = int(input("DIGITE O TERCEIRO NÚMERO: "))

    # if num1 >= num2 and num1 >= num3:
    #     print(f"{num1} É O MAIOR")
    #     print(f"{num2} É O MENOR" if num2 <= num3 else f"{num3} É O MENOR")
    # elif num2 >= num1 and num2 >= num3:
    #     print(f"{num2} É O MAIOR")
    #     print(f"{num1} É O MENOR" if num1 <= num3 else f"{num3} É O MENOR")
    # else:
    #     print(f"{num3} É O MAIOR")
    #     print(f"{num1} É O MENOR" if num1 <= num2 else f"{num2} É O MENOR")

    numbers = []

    for i in range(3):
        numbers.append(int(input(f"DIGITE O {i + 1}º NÚMERO: ")))

    print(f"{max(numbers)} É O MAIOR")
    print(f"{min(numbers)} É O MENOR")
