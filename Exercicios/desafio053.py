frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()   #mandei o split para gera uma lista
junto = ''.join(palavras)  #juntei tudo com o join depois do split
#inverso = ''
inverso = junto[::-1]   # junto começa no inicio , terminar no fim e -1 (de atras para frente)
'''for letra in range(len(junto) - 1, -1, -1):  # fiz o inverso dela , fui da ultima letra e voltei ao contrario
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não e um palindromo')