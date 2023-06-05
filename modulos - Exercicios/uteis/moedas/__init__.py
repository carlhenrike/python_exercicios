def dobro(preco=0, formato=False):
    result = preco * 2
    return result if formato is False else moeda(result)


def aumentar(preco=0, taxa=0, formato=False):
    """

    :param preco:Digitar o valor do produto
    :param taxa: digitar valor da taxa de juros
    :param formato:
    :return:
    """
    result = preco + (preco * taxa / 100)
    return result if formato is False else moeda(result)


def diminuir(preco=0, taxa=0, formato=False):
    result = preco - (preco * taxa / 100)
    return result if not formato else moeda(result)


def metade(preco=0, formato=False):
    result = preco / 2
    return result if formato is False else moeda(result)


def moeda(preco, moeda="R$"):
    return f"{moeda} {preco:.2f}".replace(".", ",")


def resumo(preco=0, aumento=0, diminuicao=0):
    result = f"""
Preço analisado: {moeda(preco)}
Dobro do preço: {dobro(preco, True)}
Metade do preço: {metade(preco, True)}
{aumento}% de aumento: {aumentar(preco, aumento, True)}
{diminuicao}% de redução: {diminuir(preco, diminuicao, True)}
    """
    return result
