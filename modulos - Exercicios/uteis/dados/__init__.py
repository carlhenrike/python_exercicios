def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f"\033[0;31mErro: '{entrada}' é um preço inválido\033[m")
        else:
            valido = True
            return float(entrada)


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
