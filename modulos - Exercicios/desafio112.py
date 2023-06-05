from uteis.moedas import resumo
from uteis.dados import leiaDinheiro

p = leiaDinheiro('Qual o valor do produto: R$')
d = int(input('Qual o valor do desconto? '))
j = int(input('Qual valor do juros? '))


print(resumo(p, d, j))