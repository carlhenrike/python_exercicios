import moedav2

p = float(input('Qual o valor do produto: R$'))
d = int(input('Qual o valor do desconto? '))
j = int(input('Qual valor do juros? '))


print(f'A metade do valor é {moedav2.metade(p, True)}')
print(f'A dobro do valor é {moedav2.dobro(p, True)}')
print(f'Aumentando {j}, temos R${moedav2.aumentar(p, j, True)}')
print(f'Descontando {d}, temos R$ {moedav2.diminuir(p, d, True)}')