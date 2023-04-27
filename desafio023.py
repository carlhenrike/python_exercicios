#import random
num = int(input('Digite um número: '))
#num = int(input(random.randint(0, 9999)))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('{} \n{} \n{} \n{}'.format(m, c, d, u))

'''n = str(num)
print(n[0])
print(n[1])
print(n[2])
print(n[3])'''



