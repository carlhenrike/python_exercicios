lista = []
lista_par = []
lista_impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, n in enumerate(lista):
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
print(f'Os valores digitado foram {lista}')
print(f'os numeros pares listado foram {lista_par}')
print(f'os numeros pares listado foram {lista_impar}')