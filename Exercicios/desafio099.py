from time import sleep
from random import randint
def maior(*num):
    cont = maior = 0
    print('\nAnalisando numeros...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


# programa principal
maior(3, 7, 8, 9, 7)
maior(3, 7, 8, 7)
maior(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
