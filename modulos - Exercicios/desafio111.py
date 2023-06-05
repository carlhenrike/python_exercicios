from uteis.moedas import resumo

p = float(input('Qual o valor do produto: R$'))
d = int(input('Qual o valor do desconto? '))
j = int(input('Qual valor do juros? '))


print(resumo(p, d, j))