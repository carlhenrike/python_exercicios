km = float(input('Kilometros percorridos:'))
qdias = int(input('Dias de locação:'))
vcar = qdias * 60
kmr = km * 0.15
vt = vcar + kmr
print('Valor da diaria: {} \nValor de KM rodado: {} \nValor Total: {}'.format(vcar, kmr, vt))
