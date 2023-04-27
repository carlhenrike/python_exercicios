v = float(input('Qual Velocidade do carro na estrada? '))
if v > 80:
    m = (v - 80) * 7
    print('Você foi multado , o valor da multa será R$ {:.2f}'.format(m))
print('Dirija com cuidado')