from random import randint
print('PAR OU IMPAR')
v = 0
while True:
    num = int(input('Diga um numero: '))
    comp = randint(0, 10)
    total = num + comp
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Escolher par ou impar? ')).upper().strip()[0]
    print(f'Voce jogou {num} e o computador {comp}. Total deu {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if escolha == 'P':
        if total % 2 == 0:
            print('Jogador Ganhou')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Jogador Ganhou')
            v += 1
        else:
            print('Jogador perdeu')
            break
    print('Vamos jogar novamente...')
print(f'Voce teve {v} vitorias')

