from random import randint
print('VAMOS JOGAR PAR OU ÍMPAR')
contador= soma = 0
escolha = ''
while True:
    computador = randint(0,11)
    nu = int(input('Diga um valor: '))
    soma = nu + computador
    escolha = str(input('Par ou Ímpar? [P/I] '))
    if escolha in 'Ii' and soma % 2 == 1 :
        print(f'Você escolheu {nu} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        contador += 1
    elif escolha in 'Pp' and soma % 2 == 0:
        print(f'Você escolheu {nu} e o computador {computador}. Total de {soma} DEU PAR')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        contador += 1
    else:
        break
print(f'GAME OVER! Você venceu {contador} vez')

