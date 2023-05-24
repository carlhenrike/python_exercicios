lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')     # Tuplas são imutaveis
#for comida in lanche:
#    print(f'Eu vou comer {comida}')
#print('Estou Cheio')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
print('Estou Cheio')