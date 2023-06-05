num = [2,5,9,1]  # lista devem ser colocadas entre colchetes
num[2] = 3  # mutação de valor de listas
num.append(7)  # adicionar valor na listas na ultima posição
num.sort()   # colcoca a lista em ordem crescente
num.sort(reverse=True)   # colcoca a lista em ordem decrescente
num.insert(2, 0)  # adicionar valor em uma posição especifica exem: 2 e a posição e 0 e o valor
num.pop(2)  # remoção do ultimo valor se adicionar nada no paretenses, mas caso queira um especifico coloco a posição do valor  entre parenteses
num.remove(2)  # remove o valor indicado pelo conteudo, sempre remove a primeira ocorrencia , dependendo do laços
del num[2]  # remove pela posição da variavel
print(num)
print(f'Essa lista tem {len(num)} elementos') # quantidade de valores