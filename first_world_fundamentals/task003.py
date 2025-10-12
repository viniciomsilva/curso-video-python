# 003
# FAÇA UM PROGRAMA QUE LEIA DOIS NÚMEROS E MOSTRE A SOMA ENTRE ELES

from custom import customize

if __name__ == "__main__":
    num1 = float(input("NÚMERO #1: "))
    num2 = float(input("NÚMERO #2: "))

    print(
        "A SOMA É: {}{}".format(
            customize(style="bold", color="cyan"),
            (num1 + num2),
        )
    )
