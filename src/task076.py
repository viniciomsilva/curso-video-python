# 076
# Crie um programa que tenha uma tupla única com nomes de produtos e seus
# respectivos preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.

from scripts.database import read_csv


def __line(l: int = 40, c: str = "-") -> str:
    return c * l


if __name__ == "__main__":
    products: list[dict[str, str | float]] = [
        {
            "name": p[0].upper(),
            "price": float(p[1]),
        }
        for p in read_csv("products.csv")
    ]

    print(__line())
    print("{:^40}".format("LISTA DE PREÇOS"))
    print(__line())

    for p in products:
        print(
            "{:.<28} R$ {:>8.2f}".format(
                p["name"],
                p["price"],
            )
        )

    print(__line())
