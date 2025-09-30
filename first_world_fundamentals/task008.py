# 008
# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E MOSTRE-O EM CENTÍMETROS E
# MILÍMETROS

num = float(input("DIGITE UM VALOR EM METROS: "))

print()
print("EM QUILÔMETROS: {}km".format(num / 1000))
print("EM HECTÔMETROS: {}hm".format(num / 100))
print("EM DECÂMETROS.: {}dac".format(num / 10))
print("EM DECÍMETROS.: {:.0f}dc".format(num * 10))
print("EM CENTÍMETROS: {:.0f}cm".format(num * 100))
print("EM MILÍMETROS.: {:.0f}mm".format(num * 1000))
