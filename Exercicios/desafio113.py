def leia_int(msg):
    while True:
        try:
            numero = int(input(f"{msg}"))
        except (ValueError, TypeError):
            print('ERRO: Por favor digite um numero inteiro valido')
            continue
        except (KeyboardInterrupt):
            print('\nUsuario não quis digitar!')
            return 0
        else:
            return numero


n = leia_int("Digite um número: ")
print(f"Você acabou de digitar o número: {n}.")
