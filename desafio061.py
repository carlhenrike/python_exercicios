pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
tm = pt
cont = 1
while cont <= 10:
    print('{} >'.format(tm), end='')
    tm += r
    cont += 1
print('FIM')
