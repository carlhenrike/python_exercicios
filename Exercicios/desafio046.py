from time import sleep
import emoji

print('CONTAGEM REGRESSIVA')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
#print('🎇' * 20)
print(emoji.emojize(':sparkler:') * 20)
