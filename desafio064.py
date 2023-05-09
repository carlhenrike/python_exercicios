n = quant = soma = 0
while n != 999:
    n = int(input('Digite um numero inteiro: '))
    if n != 999:
        quant += 1
        soma = soma + n
print('{} foi quantidade de numeros digitados e {} e a soma dos numeros digitados'.format(quant, soma))



