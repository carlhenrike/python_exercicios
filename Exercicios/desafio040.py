nota1 = float(input('Nota da prova 1: '))
nota2 = float(input('Nota da prova 2: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('REPROVADO')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÂO')
elif media >= 7:
    print('APROVADO')
print(media)
