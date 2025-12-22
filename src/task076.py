# 076
# Crie um programa que tenha uma tupla única com nomes de produtos e seus
# respectivos preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.


def run():
    names = (
        {"name": "LÁPIS PRETO", "price": "1.5"},
        {"name": "CADERNO", "price": "16.9"},
        {"name": "RESMA A4", "price": "35"},
        {"name": "LAPISEIRA 0.7", "price": "3.85"},
        {"name": "CLIPS 2/0", "price": "5.9"},
        {"name": "CANETA", "price": "2.5"},
        {"name": "BORRACHA", "price": "2.1"},
        {"name": "LÁPIS DE COR", "price": "19.75"},
        {"name": "CANETA HIDRO", "price": "21.9"},
    )

    print("-" * 40)
    print("{:^40}".format("LISTA DE PREÇOS"))
    print("-" * 40)
    for name in names:
        print(
            "{:.<28} R$ {:>8.2f}".format(
                name["name"],
                float(name["price"]),
            )
        )
    print("-" * 40)


if __name__ == "__main__":
    run()
