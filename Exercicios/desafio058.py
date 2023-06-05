from random import randint
from time import sleep
n = 0
cont = 0
cn = randint(0, 10)
print('=' * 18)
print('ADIVINHE O NÙMERO')
print('=' * 18)
while n != cn:
    n = int(input('Qual número o computador escolheu de 0 a 10? '))
    print('LENDO...')
    sleep(2)
    if n != cn:
        if cn > n:
            print('Mais... Tente de novo')
        else:
            print('Menos... Tente de novo')
    if n == cn:
        print('Tu é o Cara!')
    cont += 1
print('O computador escolheu o numero {} e você o número {} em {} tentativas.'.format(cn, n, cont))
print('=' * 18)
print('END GAME!')
print('=' * 18)
