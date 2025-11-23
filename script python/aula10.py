"""nome = str(input('Digite seu nome: ')).capitalize()
if nome == 'Nando':
    print('seu nome é muito lindo!')
else:
    print('Seu nome é tão normal!')
print('bom dia, {}!'.format(nome))"""
#---------------------------------------------------------------
nota1 = float(input('Digita sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua média foi {:.1f}.'.format(media))
if media >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruin! Estude mais!')
