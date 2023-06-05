def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# prog principal
texto = str(input('Digite algo: '))
escreva(texto)
