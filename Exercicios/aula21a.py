def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 =fatorial(5)
f2 =fatorial(4)
print(f1, f2)