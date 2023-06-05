numero = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º numero: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
print(f'Os numero pares são {sorted(numero[0])}')
print(f'Os numeros impares são {sorted(numero[1])}')