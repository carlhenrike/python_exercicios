from random import randint
from time import sleep
print('=' * 20)
print('JO KEN PÔ')
print('=' * 20)
itens = ('Pedra', 'Tesoura', 'Papel')
computador = randint(0, 2)
print('\nComputador está fazendo sua jogada...')
sleep(5)
print('\nE a sua vez!!!')
print('''Escolha a sua opção 
[0] - PEDRA 
[1] - TESOURA 
[2] - PAPEL ''')
humano = int(input('Qal a sua jogada? '))

print('Computador jogou {}'.format(itens[computador]))
print('Humano jogou {}'.format(itens[humano]))
if computador == 0 and humano == 0:
    print('\nDEU EMPATE!!!')
elif computador == 1 and humano == 0:
    print('\nCOMPUTADOR VENCEU!!!')
elif computador == 2 and humano == 0:
    print('\nVOCÊ VENCEU!!!')
elif computador == 0 and humano == 1:
    print('\nCOMPUTADOR VENCEU!!!')
elif computador == 1 and humano == 1:
    print('\nEMPATE!!!')
elif computador == 2 and humano == 1:
    print('\nVOCÊ VENCEU!!!')
elif computador == 0 and humano == 2:
    print('\nVOCÊ VENCEU!!!')
elif computador == 1 and humano == 2:
    print('\nCOMPUTADOR VENCEU!!!')
elif computador == 2 and humano == 2:
    print('\nEMPATE!!!')
