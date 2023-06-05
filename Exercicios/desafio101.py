def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não Vota'
    elif 18 > idade >= 16 or idade > 65:
        return f'Com {idade} anos: Voto Opcional'
    elif idade >= 18:
        return f'Com {idade} anos: Voto obrigatorio.'


nasc = int(input('Em que ano voce neaceu? '))
print(voto(nasc))
