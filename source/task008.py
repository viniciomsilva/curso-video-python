# 008
# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E MOSTRE-O EM CENTÍMETROS E
# MILÍMETROS


def run():
    num = float(input("Digite um valor em metros: "))

    print("Em quilômetros: {}km".format(num / 1000))
    print("Em hectômetros: {}hm".format(num / 100))
    print("Em decâmetros.: {}dac".format(num / 10))
    print("Em decímetros.: {:.0f}dc".format(num * 10))
    print("Em centímetros: {:.0f}cm".format(num * 100))
    print("Em milímetros.: {:.0f}mm".format(num * 1000))
