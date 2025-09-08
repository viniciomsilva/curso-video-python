# 010
# CRIEI UM CONVERSOR DE REAL PARA DÓLAR

brlUsd = 5.3962
brlEur = 6.3449
# Fonte: BCB (5/9/25)

brl = float(input('DIGITE UM VALOR EM R$: '))

print('BRL R$ {:.4f} = USD US$ {:.4f}'.format(brl, (brl / brlUsd)))
print('BRL R$ {:.4f} = EUR   € {:.4f}'.format(brl, (brl / brlEur)))
