a =[2, 3, 4, 7]
b = a[:]   # dessa forma não a ligação entre as lista a lis B vira uma copia da lista A
b[2] = 8
print(f'Lista A : {a}')
print(f'Lista A : {b}')