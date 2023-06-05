pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
q = int(input('Quantas vezes sera exibido ?'))
tm = pt + r * (q - 1)
for c in range(pt, tm + 1, r):
    t = pt + r
    print(c)
