def leiaInt(msg):
    while True:
        try:
            n = int(input(f"{msg}"))
        except (ValueError, TypeError):
            print('ERRO: Por favor digite um numero inteiro valido')
            continue
        except KeyboardInterrupt:
            print('\nUsuario não quis digitar!')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc
