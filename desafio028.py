from random import randint
from time import sleep
cn = randint(0, 5)
print('=' * 18)
print('ADIVINHE O NÙMERO')
print('=' * 18)
n = int(input('Qual número o computador escolheu de 0 a 5? '))
print('LENDO...')
sleep(3)
if n == cn:
    print('Tu é o Cara!')
else:
    print('Deu mole! O número era {} e você escolheu {}.'.format(cn, n))
print('=' * 18)
print('END GAME!')
print('=' * 18)
