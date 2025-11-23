tupla = ('zero','um','dois', 'três','quatro',
         'cinco','seis','sete','oito','nove',
         'dez','onze','doze','treze','catorze',
         'quinze','dezesseis','dezessete','dezeito',
         'dezenove','vinte')
nu = int(input('Digite um número de 0 a 20: '))
while True:
    if nu < 0 or nu > 20:
            nu = int(input('Tente novamnete. Digite um número entre 0 e 20: '))
            continue
    else:
        print(f'Você digitou o número {tupla[nu]}')
        break

