temp = []
lista = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]


    lista.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Os dados foram {lista}')
print(f'{len(lista)} foram cadastradas.')
print(f'O Maior peso foi de {maior} do ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O Menor peso foi de {menor} do ',end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}')