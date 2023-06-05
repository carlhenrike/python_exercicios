import lib.interface


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    """

    :rtype: object
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve erro na criação do arquivo')
    else:
        print(f'Aqruivo {nome} criado com sucesso')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        lib.interface.cabecalho('PESSOAS CADASTRADAS')
        print(a.read())
