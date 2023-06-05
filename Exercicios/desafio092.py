from datetime import datetime

dados = dict()

dados["name"] = str(input("Digite um nome: "))
nasc = int(input("Data de nascimento: "))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input("Número da carteira de trabalho (CTPS): "))

if dados['ctps'] != 0:
    dados['contratação'] = int(input("Ano de contratação: "))
    dados['salário'] = int(input("Salário: R$"))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - datetime.now().year
print(dados)
