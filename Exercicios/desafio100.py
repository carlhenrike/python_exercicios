from random import randint
from time import sleep


def sorteia(lista):
    print('Valores sorteados da lista: ',end='')
    for cont in range(0, 5):
        n = randint(1, 20)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nO total da soma dos valores pares é {soma}')

numeros = list()
sorteia(numeros)
somapar(numeros)
