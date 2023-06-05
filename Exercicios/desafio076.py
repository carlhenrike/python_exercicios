lista = ('Lápis', 1.75,
         'Caneta', 3.00,
         'Caderno', 10.00,
         'Mochila', 115.90)
print('-----------------------------')
print('      LISTA DE PREÇOS        ')
print('-----------------------------')
for posicão_var in range(0, len(lista)): # usa o range para quando for escolher a posição da variavel na tupla
    if posicão_var % 2 == 0:
        print(f'{lista[posicão_var]:.<25}', end='')
    if posicão_var % 2 == 1:
        print(f'R${lista[posicão_var]:>10}')

