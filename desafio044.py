from time import sleep
from random import uniform
preco_normal = (round(uniform(100, 10000), 2))

dinheiro_cheque = preco_normal - (preco_normal * (10 / 100))
avista_cartao = preco_normal - (preco_normal * (5 / 100))
cartao_2x = preco_normal
cartao_3x = preco_normal + (preco_normal * (20 / 100))

decisao = int(input('''Escolha \n
1 - Valor á vista no dinheiro / cheque com 10 % de desconto
2 - Valor á vista no cartão com 5% de desconto''
3 - Valor em até 2X no cartão no preço normal 
4 - Valor em 3 x ou mais no cartão com 20% de juros 

Digite: '''))
sleep(2)

if decisao == 1:
    print(' O valor do produto é {:.2f} , com desconto ficará {:.2f}'.format(preco_normal, dinheiro_cheque))
elif decisao == 2:
    print(' O valor do produto é {:.2f} , com desconto ficará {:.2f}'.format(preco_normal, avista_cartao))
elif decisao == 3:
    print(' O valor do produto será {:.2f} '.format(cartao_2x))
elif decisao == 4:
    print(' O valor do produto é {:.2f} , com o juros acrescido ficará {:.2f}'.format(preco_normal, cartao_3x))
