n = int(input('Digite um número:'))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        total += 1  # vai dizer por quantos numeros ele e divisivel
print('{} é divisivel {} vezes'.format(n,total))
if total == 2:
    print('Ele é número primo')
else:
    print('Não um numero primo')