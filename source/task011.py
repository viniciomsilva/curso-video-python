# 011
# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS.
# CALCULE SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE
# CADA 1L DE TINTA PINTA UMA ÁREA DE 2M²

from scripts.custom import customize


def run():
    width = float(input("Digite a largura em metros: "))
    height = float(input("Digite a altura em metros.: "))

    area = width * height

    print(
        "Você precisará de {} de tinta para pintar uma área de {}".format(
            customize(
                "{:.1f}L".format(area / 2),
                style="under",
                color="cyan",
            ),
            customize(
                "{:.2f}m²".format(area),
                style="under",
                color="magenta",
            ),
        )
    )
