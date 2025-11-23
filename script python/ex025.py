nome = str(input('Digite seu nome: ')).strip()
pm = nome.title() # serve para colocar toda primeira letra de cada palavra em maiuscula
ind = 'Silva' in pm # serve para indentificar uma palavra especifica
print (ind)


nome = str(input('Digite seu nome: ')).strip()
print('Seu nome tem Silva {}'.format('SILVA' in nome.upper()))