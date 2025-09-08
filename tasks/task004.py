# 004
# FAÇA UM PROGRAMA QUE LEIA ALGO DO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITICO
# E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE

anyValue = input('DIGITE ALGUMA COISA.: ')

print('TIPO.........:', type(anyValue))
print('ESPAÇO.......:', anyValue.isspace())
print('MINÚSCULO....:', anyValue.islower())
print('MAIÚSCULO....:', anyValue.isupper())
print('CAPITALIZADO.:', anyValue.istitle())
print('ALFANUMÉRICO.:', anyValue.isalpha())
print('NUMÉRICO.....:', anyValue.isnumeric())
print('DECIMAL......:', anyValue.isdecimal())
