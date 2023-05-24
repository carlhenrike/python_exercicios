numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
           int(input('Digite o ultimo número: ')))

print(f'{numeros}')
print(f'O numero 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f"O numero 3 esta na posicao {numeros.index(3) + 1}")
else:
    print('O valor 3 não foi digitado')
for n in numeros:  # usar for com in quando não precisar contar variavel na tupla
    if n % 2 == 0:
        print(f'O numero par digitado foi {n}')
