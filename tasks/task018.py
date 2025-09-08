# 018
# FAÇA UM PROGRAMA QUE LEIA O VALOR DE UM ÂNGULO QUALQUER E MOSTRE NA TELA OS VALORES DO SENO, COSSENO E TANGENTE

from math import sin, cos, tan, radians #, pi

angle = float(input('DIGITE UM ÂNGULO: '))

# radians = angle / 180 / pi

print()
print('SIN({:.1f}º) = {:.6f}'.format(angle, sin(radians(angle))))
print('COS({:.1f}º) = {:.6f}'.format(angle, cos(radians(angle))))
print('TAN({:.1f}º) = {:.6f}'.format(angle, tan(radians(angle))))
