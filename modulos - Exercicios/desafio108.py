import moedav1

p = float(input('Qual o valor do produto: R$'))
d = int(input('Qual o valor do desconto? '))
j = int(input('Qual valor do juros? '))


print(f'A metade do valor é {moedav1.moeda(moedav1.metade(p))}')
print(f'A dobro do valor é {moedav1.moeda(moedav1.dobro(p))}')
print(f'Aumentando {j}, temos R${moedav1.moeda(moedav1.aumentar(p, j))}')
print(f'Descontando {d}, temos R$ {moedav1.moeda(moedav1.diminuir(p, d))}')