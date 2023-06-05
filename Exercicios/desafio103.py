def ficha(nome_jogador, numero_gols):
    return f"O jogador {nome_jogador.upper()} fez {numero_gols} gols."


nome = str(input("Nome do jogador: "))
if len(nome) == 0:
    nome = "<desconhecido>"

gols = str(input("Número de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
print(ficha(nome, gols))