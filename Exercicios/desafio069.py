tot18 = totH = totM20 = 0
while True:
    idade = int(input('Digite su idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M / F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Mulheres com menos de 20 ano {totM20}')
print(f'Homens tem {totH}')
print(f'Menos de 18 anos {tot18}')