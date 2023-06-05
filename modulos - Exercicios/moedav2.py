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


def moeda(num, moeda="R$"):
    return f"{moeda} {num:.2f}".replace(".", ",")


