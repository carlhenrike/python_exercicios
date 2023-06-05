def dobro(preco):
    return preco * 2


def aumentar(preco, taxa):
    return preco + (preco * taxa / 100)


def diminuir(preco, taxa):
    return preco - (preco * taxa / 100)


def metade(preco):
    return preco / 2


def moeda(num, moeda="R$"):
    return f"{moeda} {num:.2f}".replace(".", ",")