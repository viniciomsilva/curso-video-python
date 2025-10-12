# 011
# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS.
# CALCULE SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE
# CADA 1L DE TINTA PINTA UMA ÁREA DE 2M²

from custom import clear
from custom import customize

if __name__ == "__main__":
    width = float(input("DIGITE A LARGURA EM METROS: "))
    height = float(input("DIGITE A ALTURA EM METROS.: "))

    area = width * height

    print(
        "VOCÊ PRECISARÁ DE {}{:.1f}L{} DE TINTA PARA PINTAR UMA ÁREA DE {}{:.2f}m²".format(
            customize(style="bold", color="cyan"),
            (area / 2),
            clear(),
            customize(style="bold", color="lilac"),
            area,
        )
    )
