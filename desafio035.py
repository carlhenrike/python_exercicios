l1: float = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3: float = float(input('Digite o terceiro lado: '))
tri = l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2
print('POde formar um triangulo? {}'.format(tri))
if l1 == l2 and l2 == l3:
    print('E um triangulo equilatero')
elif l1 == l2 or l2 == l3 or l1 == l3:
        print('E um triangulo isosceles')
else:
    l1 != l2 and l2 != l3 and l1 != l3
    print('O triangulo é Escaleno')