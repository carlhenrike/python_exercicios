from datetime import date
nascimento = int(input('Qual é a data de nascimento do atleta? '))
idade = date.today().year - nascimento
if idade <= 9:
    print('Você tem {} anos , a sua categoria é Mirim'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, a sua categoria é Infantil'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, sua categoria é Junior'.format(idade))
elif idade <= 25:
    print('Você tem {} anos,  sua categoria é Sênior'.format(idade))
else:
    print('Você tem {} anos, sua categoria e Master'.format(idade))