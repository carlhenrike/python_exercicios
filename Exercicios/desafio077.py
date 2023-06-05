palavras = 'Carlos', 'Sheila', 'Bruno', 'Pepinha'
vogais = 'aeiou'
for n in palavras:
        print(f'\nNa palvara {n} temos: ', end='')
        for letra in n:
            if letra.lower() in vogais:
                    print(letra, end=' ')
