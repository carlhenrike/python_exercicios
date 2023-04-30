from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento
q_tempo_falta = 18 - idade
q_tempo_passou = idade - 18
ano_alistamento = date.today().year - q_tempo_passou
ano_alistamento_falta = date.today().year - q_tempo_falta
if idade == 18:
    print('Você já tem {} anos, chegou a hora de se alistar'.format(idade))
elif idade < 18:
    print('Voce ainda tem {} anos , ainda vai se alistar daqui há {} anos, no ano de {}'.format(idade, q_tempo_falta, ano_alistamento_falta))
elif idade > 18:
    print('Voce ja tem {} anos já passou o tempo de alistamento há {} anos , no ano de {}'.format(idade, q_tempo_passou, ano_alistamento))
