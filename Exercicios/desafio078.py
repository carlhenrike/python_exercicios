valores = []
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um Valor na posição {cont+1}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'O maior numero da lista é {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i+1}... ', end='')
print()
print(f'O menor numero da lista é {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i+1}... ', end='')
print()
