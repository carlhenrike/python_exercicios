n = int(input('Digite um número inteiro: '))
# binario = bin(n)
# octal = oct(n)
# hexadecimal = hex(n)
escolha = int(input('Escolha: \n1 para binario \n2 para octal \n3 para hexadecimal \n\nDigite: '))
if escolha == 1:
    print('{} em binario é {}'.format(n, bin(n)))
elif escolha == 2:
    print('{} em octal é {}'.format(n, oct(n)))
elif escolha == 3:
    print('{} em hexadecimal é {}'.format(n, hex(n)))
