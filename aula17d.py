valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))  # adicionar valor na listas na ultima posição ou adiciona dependendo caso não haver valor .
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao Final da lista')