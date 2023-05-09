num = 0
continuar = 'S'
media = cont = quant = maior = menor = 0
while continuar != 'N':
    num = int(input('Digite um número: '))
    cont += 1
    quant = quant + num
    media = quant / cont
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
           menor = num
    continuar = input('Deseja continuar? [S/N]').upper().strip()[0]
print('A Media do numeros é {:.2f} , o maior numero é {} e o menor é {}'.format(media, maior, menor))
print('foram digitados {} numeros'.format(cont))
