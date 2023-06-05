
totG = M1000 = menor = cont = 0
barato = ' '
while True:
    p = str(input('Qual produto foi comprado? '))
    v = float(input('Qual o valor do produto? R$'))
    cont += 1
    totG += v
    if v > 1000:
        M1000 += 1
    if cont == 1 or v < menor:
        menor = v
        barato = p
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? ')).upper().strip()[0]
    if resp == 'N':
        break
print(f' Valor total que foi gasto foi R${totG:.2f}')
print(f'{M1000} foi o produto com valor maior que R$ 1000')
print(f'O {barato} foi produto com   menor valor é custou R${menor}')