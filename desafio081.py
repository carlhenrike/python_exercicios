lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f"{len(lista)} elementos foram digitados")
lista.sort(reverse=True)
print(f'A lista em forma decrescente vai ser {lista}')
if 5 in lista:
    print('O numero 5 esta na lista')
else:
    print('O numero 5 não esta lista')