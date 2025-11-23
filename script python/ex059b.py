from time import sleep
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print("""[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos valores
[ 5 ] Sair """)
    opcao = int(input('>>>>> Qual é sua opção? '))
    if opcao == 1:
        soma = primeiro + segundo
        print(f'A soma entre {primeiro} + {segundo} é igual a {soma}')
    elif opcao == 2:
        mult = primeiro * segundo
        print(f'A multiplicação de {primeiro} x {segundo} é igual a {mult}')
    elif opcao == 3:
        if primeiro > segundo:
            print(f'O número {primeiro} é maior que {segundo}')
        elif primeiro < segundo:
            print(f'O número {primeiro} é menor que {segundo}')
        else:
            print(f'Os números informados tem o mesmo valor {primeiro}')
    elif opcao == 4:
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')


