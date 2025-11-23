from random import randint     #
contador = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o compuatdor {computador}. Total de {soma} ', end='')
    print('DEU PAR ' if soma % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            contador += 1
        else:
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            contador += 1
        else:
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER, Você venceu {contador} vezes')