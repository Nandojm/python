
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))
if ano == 0 :
    ano = date.today().year # esta importação pega o ano atual do computador
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('O ano que você nasceu é um ano bissexto:')
else:
    print('O ano que você nasceu não é um ano bissexto.')