total_idades = 0
media = 0
menos_20 = 0
maior = 0
nome_velho = 0
for c in range(1, 4 + 1):
    print('PESSOA {}'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade '))
    sexo = str(input('Sexo [m/f}: '))
    total_idades = total_idades + idade
    media = total_idades / c
    if idade > maior and sexo == 'm':
        maior = idade
        nome_velho = nome
    if sexo == 'f' and idade < 20:
        menos_20 = menos_20 + 1

print('A media do grupo é {}, o nome do homem mais velho é {} é {} mulheres tem menos que 20 anos'.format(media, nome_velho, menos_20))