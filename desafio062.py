pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
tm = pt
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print('{} >'.format(tm), end='')
        tm += r
        cont += 1
    print('Pausa')
    mais = int(input('\nDeseja mostrar mais quantos?'))
print('{} foi tota de termo solicitados)'.format(total))