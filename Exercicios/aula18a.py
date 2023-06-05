teste = list()
teste.append('Gustavo') # adição da variavel
teste.append(40)
galera = list()    # outras lista
galera.append(teste[:])  # inserção e copia  da lista teste na lista galera , [:] cria uma copia independente da lista original
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])   # adicionando e copia da variaveis maria e 22 substuituindo os valores
print(galera)
