#from math import pow, sqrt
import math

n1 = float(input('Digite o valor do cateto: '))
n2 = float(input('Digite o valor do cateto adjacente: '))
#h = sqrt(pow(n1, 2) + pow(n2, 2))
#h = math.sqrt(math.pow(n1, 2) + math.pow(n2, 2))
h = math.hypot(n1, n2)
print('O comprimento da hipotenusa será: {:.2f}'.format(h))
