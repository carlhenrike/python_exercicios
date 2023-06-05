import moedav3

p = float(input('Qual o valor do produto: R$'))
d = int(input('Qual o valor do desconto? '))
j = int(input('Qual valor do juros? '))


print(moedav3.resumo(p, d, j))