s = 0
cont = 0
for c in range(1, 500):
    if c % 3 == 0 and c % 2 != 0:
        cont = cont + 1  # contador adiciona mais 1
        s = s + c        # acumulador sempre a acumula e soma
print('O total de {} valores da soma é {}'.format(cont, s))

