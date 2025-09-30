# 014
# ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA EM ºC PARA ºF

celsius = float(input("DIGITE A TEMPERATURA EM ºC: "))

fahrenheit = celsius * 9 / 5 + 32

print("{:.1f}ºC = {:.1f}ºF".format(celsius, fahrenheit))
