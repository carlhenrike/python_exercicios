from datetime import date
ano = int(input('Digite um ano ou ano atual digitando 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano e bissexto')
else:
    print('Esse ano não e bissexto')

