km = float(input('Qual a distancia da viagem? '))
if km <= 200:
    p = km * 0.50
else:
    p = km * 0.45
print('Valor da pasagem será {:.2f}'.format(p))

