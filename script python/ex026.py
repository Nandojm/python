txt = str(input('Digite uma palavra: ')).strip().upper()
print('A letra A aparece {} vezes na palvra'.format(txt.count('A')))
print('A primeira letra A apareceu na posição {}'.format(txt.find('A')+1))
print('A ultima letra aparece na posição {}'.format(txt.rfind('A')+1))