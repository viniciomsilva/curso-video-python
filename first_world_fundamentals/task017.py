# 017
# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DOS CATETOS OPOSTO E ADJACENTE
# DE UM TRIANGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

from math import hypot  # , sqrt

a = float(input("DIGITE O VALOR DE A: "))
b = float(input("DIGITE O VALOR DE B: "))

# hypotenuse = sqrt((pow(a, 2) + pow(b, 2)))

print("A HIPOTENUSA VALE..: {:.2f}".format(hypot(a, b)))
