nome = str(input('Digite seu nome? ')).format().capitalize()
if nome == 'Nando':
    print('Que nome bonito!')
elif nome == 'Paulo' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é muito popular no Brasil.')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é tão normarl.')
print('Tenha um bom dia, {}!'.format(nome))