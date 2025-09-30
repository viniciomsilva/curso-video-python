# 006
# CRIE UM PROGRAMA QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, O TRIPLO E A RAIZ
# QUADRADA

from math import sqrt

num = int(input("DIGITE UM NÚMERO INTEIRO: "))

print("DOBRO........: {}".format(num * 2))
print("TRIPLO.......: {}".format(num * 3))
# print('RAIZ QUADRADA: {}'.format(pow(num, 0.5)))
print("RAIZ QUADRADA: {:.2f}".format(sqrt(num)))
