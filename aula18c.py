galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()   # para remove da dado duplicado no print
print(galera)