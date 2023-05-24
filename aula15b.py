n = s =0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s = s + n
# print('A soma é {}'.format(s)) # python 3
print(f'A soma é {s}')  # python 3.6
print('A soma é %s' % (s))  # python 2