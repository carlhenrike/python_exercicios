expr = str(input('Digite a expressão: '))
pillha = []
for simb in expr:
    if simb == '(':
        pillha.append('(')
    elif simb == ')':
        if len(pillha) > 0:
            pillha.pop()
        else:
            pillha.append(')')
            break
if len(pillha) == 0:
    print('Expressão correta')
else:
    print('Expressao esta errada')


