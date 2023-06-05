extensos = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito",
    "nove", "dez", "onze", "doze", "treze", "catorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
    )
while True:
    n = int(input("Digite um número de 0 a 20: "))
    if 0 <= n <= 20:
        print(f"Você digitou: {extensos[n]}.")
        break
    else:
        print("Tente novamente.", end=" ")