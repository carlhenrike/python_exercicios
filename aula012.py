nome = str(input('Qual e seu nome? '))
if nome == 'Carlos':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Bruno':
    print('Seu nome e pupular no Brasil.')
elif nome in 'Sheila Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome e bem normal')
print('Tenha um bom dia, {}!'.format(nome))