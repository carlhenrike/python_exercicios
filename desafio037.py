from time import sleep
n = int(input('Digite um número inteiro: '))
# binario = bin(n)
# octal = oct(n)
# hexadecimal = hex(n)
escolha = int(input('''Escolha:
1 para binario
2 para octal
3 para hexadecimal

Digite: '''))
sleep(3)
if escolha == 1:
    print('{} em binario é {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('{} em octal é {}'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('{} em hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção Invalida')