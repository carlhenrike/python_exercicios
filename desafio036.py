valor_casa = float(input('Qual valor da casa que você deseja comprar? '))
salario = float(input('Qual e o seu salario mensal? '))
anos_pagar = int(input('Em quantos anos deseja levar para pagar?'))

parcelas = valor_casa / (anos_pagar * 12)
valor_excedente = salario * (30 / 100)
if parcelas > valor_excedente:
    print('Desculpe seu emprestimo foi negado pois o valor da parcela excede o valor de 30% do seu salario')
else:
    print('Seu emprestimo foi liberado')
