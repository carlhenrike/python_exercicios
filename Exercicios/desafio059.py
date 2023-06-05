n1 = int(input('Digite o valor 1:'))
n2 = int(input('Digite o valor 2: '))
resposta = 0
while resposta != 5:
    print('ESCOLHA UMA OPÇÃO DO MENU: ')
    print('''
          [1] Somar
          [2] Multiplicar
          [3] Maior Número
          [4] Novos números
          [5] Sair
          ''')

    resposta = int(input('Digite sua escolha: '))
    if resposta == 1:
        print(' A soma de {} e {} é {}'.format(n1, n2, n1 + n2))
    if resposta == 2:
        print('A multiplicação de {} e {} é {}'.format(n1, n2, n1 * n2))
    if resposta == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {}'.format(n2))
    if resposta == 4:
        print('Escolha novos números:')
        n1 = int(input('Digite o valor 1:'))
        n2 = int(input('Digite o valor 2: '))
    if resposta == 5:
        print('Finalizando')
    else:
        print('Opção invalida')
print('Obrigado!')
