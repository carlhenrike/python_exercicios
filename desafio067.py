while True:
        n = int(input('Que ver a tabuada de que valor: '))
        if n < 0:
            break
        for cont in range(0, 10):  # while cont < 10:
            cont += 1
            t = n * cont
            print(f'{n} X {cont} = {t}')
