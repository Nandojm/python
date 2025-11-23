from random import randint
print('VAMOS JOGAR PAR OU ÍMPAR')
contador = nu = 0
while True:
    computador = randint(0, 11)
    try:
        nu = int(input('Digite um número: '))
    except ValueError:
        print('[ERRO] Digite apenas números')
        continue
    soma = nu + computador
    escolha = str(input('Qual você escolhe? [P/I] ')).strip().upper()
    if (escolha != 'P') and (escolha != 'I'):
        print('RESPOSTA INVALIDA! ')
    elif escolha in 'P' and soma % 2 == 0 :
        print('Você VENCEU')
        print(f'Você escolheu {nu} e o computador {computador}. Total de {soma} DEU PAR')
        print('Vamos jogar novamente...')
        contador += 1
    elif escolha in 'I' and soma % 2 == 1:
        print('Você VENCEU')
        print(f'Você escolheu {nu} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        print('Vamos jogar novamente...')
        contador += 1
    else:
        break
print(f'GAME OVER! Você venceu {contador} vez')
