#import math
from math import cos, sin, tan, radians

angulo = float(input('Digite o valor do angulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(sen, cos, tan))
