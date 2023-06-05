def leia_int(msg):
    ok = False
    valor = 0
    while True:
        numero = input(f"{msg}")
        if numero.isnumeric():
            valor = numero
            ok = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido!\033[m")
        if ok:
            break
    return valor


n = leia_int("Digite um número: ")
print(f"Você acabou de digitar o número: {n}.")