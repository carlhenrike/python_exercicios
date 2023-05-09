sexo = ''

while sexo == 'M' or 'F':
    sexo = input('Digite seu sexo: [M/F]').upper().strip()[0]
    if sexo != 'F' and sexo != 'M':
        print('Valor errado peço que digite um valor valido!', end=' ')


'''sexo = input('Digite seu sexo: [M/F]').upper().strip()[0]
while sexo not in 'MmFf':
    sexo = input('Valor valido! Digite seu sexo:').upper().strip()[0]
print('Seu Sexo {} foi registrado com sucesso '.format(sexo))'''

