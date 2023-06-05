valores = list()
while True:
    n = int(input('Digite valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor Adicionado com sucesso...')
    else:
        print('Valor Duplicado! Não possivel adicionar...')
    resp = str(input('Quer Continuar? [S/N]'))
    if resp in 'Nn':
        break
valores.sort()
print(f'Foi digitado {valores}')

