n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua media foi {:.2f}'.format(m))
if m >= 7.0:
    print('Parabens sua nota esta otima')
else:
    print('Sua nota esta abaixo da media! Estude mais!')