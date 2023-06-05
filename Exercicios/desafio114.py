import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.facebook.com.br')
except:
    print('Deu erro')
else:
    print('Deu Ok')
    print(site.read())