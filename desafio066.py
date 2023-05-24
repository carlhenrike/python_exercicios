quant = soma = 0
while True:
    n = int(input('Digite um numero inteiro: '))
    if n == 999:
        break
    quant += 1
    soma = soma + n
print('{} foi quantidade de numeros digitados e {} e a soma dos numeros digitados'.format(quant, soma))
