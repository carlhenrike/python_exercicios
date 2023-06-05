pessoas = {'nome': 'Carlos', 'sexo': 'M', 'idade': 32}
pessoas['nome'] = 'Henrique'
pessoas['peso'] = '73.5'
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
