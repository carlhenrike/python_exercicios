import moeda

p = float(input('Qual o valor do produto: R$'))
d = int(input('Qual o valor do desconto? '))
j = int(input('Qual valor do juros? '))


print(f'A metade do valor é {moeda.metade(p)}')
print(f'A dobro do valor é {moeda.dobro(p)}')
print(f'Aumentando {j}, temos R${moeda.aumentar(p, j)}')
print(f'Descontando {d}, temos R$ {moeda.diminuir(p, d)}')