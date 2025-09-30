# 011
# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS.
# CALCULE SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE
# CADA 1L DE TINTA PINTA UMA ÁREA DE 2M²

width = float(input("DIGITE A LARGURA EM METROS: "))
height = float(input("DIGITE A ALTURA EM METROS.: "))

paintedPerLiter = 2
area = width * height

print(
    "VOCÊ PRECISARÁ DE {:.1f}L DE TINTA PARA PINTAR UMA ÁREA DE {:.2f}m²".format(
        (area / paintedPerLiter), area
    )
)
