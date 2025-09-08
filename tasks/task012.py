# 012
# FAÇA UM PROGRAMA QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE-O COM 5% DE DESCONTO

price = float(input('DIGITE O VALOR DO PRODUTO...........: R$ '))
discount = float(input('DIGITE A PORCENTAGEM DE DESCONTO (%):    '))

print('\nVALOR TOTAL.........................: R$ {:.2f}'
      .format((price * (1 - discount / 100))))
