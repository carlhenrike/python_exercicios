s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s = s + n
        cont += 1
print("A soma dos {} numeros pares é {}".format(cont, s))
