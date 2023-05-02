n = int(input('Digite um numero para mostra a tabuada:'))
print('=' * 20)
print('Tabuada de {} '.format(n))
print('=' * 20)
for c in range(0, 11):
    t = n * c
    print('{} X {} = {}'.format(n, c, t))