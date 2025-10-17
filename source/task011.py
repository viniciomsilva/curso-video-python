# 011
# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS.
# CALCULE SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE
# CADA 1L DE TINTA PINTA UMA ÁREA DE 2M²

from utils import custom as cs


def run():
    width = float(input("Digite a largura em metros: "))
    height = float(input("Digite a altura em metros.: "))

    area = width * height

    print(
        "Você precisará de {} de tinta para pintar uma área de {}".format(
            cs.colorize(f"{(area / 2):.1f}L", color="cyan"),
            cs.colorize(f"{area:.2f}m²", color="lilac"),
        )
    )


if __name__ == "__main__":
    run()
