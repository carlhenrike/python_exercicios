from math import pow
peso = float(input('Digite sua peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / pow(altura, 2)
if imc < 18.5:
    print('O seu IMC está em {:.2f}, você está abaixo do peso'.format(imc))
elif 18.5 <= imc <= 25:
    print('O seu IMC esta em {:.2f}, voceê esta no peso ideal'.format(imc))
elif 25 < imc <= 30:
    print('O seu IMC esta em {:.2f}, você esta com sobrepeso'.format(imc))
elif 30 < imc <= 40:
    print('O seu IMC esta em {:.2f}, você esta com Obesidade'.format(imc))
else:
    print('O seu IMC esta em {:.2f}, você esta com obesidade mórbida'.format(imc))