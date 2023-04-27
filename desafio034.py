salario = float(input('Qual seu seu salario? '))
if salario > 1250:
    salario_novo = salario + (salario * (10 / 100))
else:
    salario_novo = salario + (salario * (15 / 100))
print('Seu salario era {} e agora sera: {}'.format(salario, salario_novo))
