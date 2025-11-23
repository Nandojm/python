cont = ('zero','um','dois', 'três','quatro',
         'cinco','seis','sete','oito','nove',
         'dez','onze','doze','treze','catorze',
         'quinze','dezesseis','dezessete','dezeito',
         'dezenove','vinte')
while True:
    nu = int(input('Digite um número entre 0 e 20: '))
    while True:
        if 0 <= nu <= 20:
           break
        else:
            print('Tente novamente. ', end='')
            nu = int(input('Digite um número entre 0 e 20: '))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print(f'Você digitou o numero {cont[nu]}')