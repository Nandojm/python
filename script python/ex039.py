import datetime
print(' ')
idade = int(input('Digite sua idade: '))

ano = datetime.date.today().year
fal = 18 - idade
numero = abs(fal)



if idade < 18:
    print('vai ter que se alistar')
    print('Seu prazo de se alistar é daqui a {} ano(s).'.format(numero))

elif idade == 18:
    print('Este ano é o seu alistamento.')
    print(ano)
elif idade > 18:
    print('Você já passou {} ano(s) do seu alistamento'.format(numero))


