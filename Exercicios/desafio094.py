galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar: [S/N]')).upper()
        if resp in 'SN':
            break
        print('ERRO responda s ou N')
    if resp == 'N':
        break
print(f'{len(galera)} pessoas foram cadastradas')
media = soma / len(galera)
print(f'´{media} é a media da pessoas.')
print('As mulheres cadastradas foram')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}')
print('Essas pessoas estao acima da media')
for p in galera:
    if p['idade'] >= media:
        print('  ')
        for k, v in p.items():
            print(f'`{k} = {v};')
        print()
