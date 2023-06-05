from datetime import date
maior = 0
menor = 0
for c in range(1, 7 + 1):
    nascimento = int(input('Digite o {}° ano de nascimento: '.format(c)))
    idade = date.today().year - nascimento
    if idade < 18:
        menor = menor + 1
    else:
        maior += 1
print('{} pessoas são maior de idade e {} são menores de idades'.format(maior, menor))

