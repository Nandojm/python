import datetime
ano = int(input('Digite que ano você nasceu: '))

print(' ')

atual = datetime.date.today().year
idade = atual - ano
if idade <= 9 :
    print('Você tem {} anos, então você esta na categoria: MIRIM.'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, então você está na categoria: INFANTIL.'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, então você está na categoria: JUNIOR.'.format(idade))
elif idade <= 22:
    print('Você tem {} anos, então você está na categoria: SENIOR.'.format(idade))
elif idade > 22:
    print(' Você tem {} anos, então você está na categoria: MASTER.'.format(idade))
print(' ')
print('Obrigado por se escrever na nossa piscina.')