import random

a1 = input('Digite nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
escolhido = [a1, a2, a3, a4]
print('O aluno escolhido foi: {}'.format(random.choice(escolhido)))
