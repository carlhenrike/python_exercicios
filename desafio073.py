brasileirao = (
    'Botafogo', 'Palmeiras', 'Fluminense', 'Atletico-MG', 'Cruzeiro', 'Flamengo', 'Athetico-PR', 'São Paulo',
    'Santos', 'Gremio', 'Fortaleza', 'Bragantino', 'Bahia', 'Cuiaba', 'Internacional', 'Goias', 'Vasco', 'Corinthians',
    'America-MG', 'Coritiba')

print(f'Os Cincos primeiros colocados são {brasileirao[:5]}')
print(f'Os Ultimos quatro times são {brasileirao[-4:]}')
print(f'A ordem alfabetica é {sorted(brasileirao)}')
print(f'O Flamengo esta na {brasileirao.index("Flamengo")+1}ª posicao')