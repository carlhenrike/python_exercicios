from random import randint
num = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'A lista de numeros foi : ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior numero é {max(num)}')
print(f'O Menor numero é {min(num)}')
