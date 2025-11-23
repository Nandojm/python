from time import sleep # importei a função sleep
primeiro = int(input('Primeiro valor: ')) # recebe o primeiro numero
segundo = int(input('Segundo valor: ')) # recebe o segundo número
opcao = 0 # iniciei a ooção com zero
sair = False # função sair em falsa
acao = 0 # resultado da ação em zero
while not  sair: # em quanto sair não for verdadeira, vai ficar realizando o looping
    print('--='* 10)
    print("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novo números
[5] Sair do programa""")
    opcao = int(input('>>>>> Qual é sua opção? ')) # aqui vai dar escolher a função com base numerica de 1 a 5
    if opcao == 5: # se o usuario escolher a opção 5
        sair = True # sair passa a ser verdadeira e fecha o programa
    if opcao == 1: # se a opção for a 1
        acao = primeiro + segundo # a acão passa a ser somar primeiro e segundo numero
        print(f'A soma entre {primeiro} e {segundo} é igual a {acao}') # e mostrar o resultado
    elif opcao == 2: # se a opção for a 2
        acao = primeiro * segundo # a ação vai multiplicar o primeiro pelo segundo número
        print('O resultado de {} x {} é {}'.format(primeiro, segundo, acao)) # mostrar o resultado
    elif opcao == 3: # se a opção for a 3
        if primeiro > segundo: # primeiro vai ver se o primeiro número é maior que o segundo número, se for
            print('Entre {} e {} o maior valor é {}'.format(primeiro, segundo, primeiro)) # vai mostrar esse resultado
        elif primeiro < segundo: # se não vai ver se o primeiro é menor que o segundo, se for
            print('Entre {} e {} o maior número é {}'.format(primeiro, segundo, segundo)) # vai mostrar este resultado
        elif primeiro == segundo: # agora se os dois numeros forem iguais
            print('Os dois números possui o mesmo valor que é {}'.format(primeiro, segundo,primeiro)) # vai mostrar este resultado
    elif opcao == 4 : # agora se for a opção 4, vai dar o opção para o usuario para trocar
        primeiro = int(input('Primeiro valor: ')) # o primeiro número
        segundo = int(input('Segundo valor: ')) # e o segundo
    elif opcao > 5:# e se o usuario digitar um numero que não esteja entre 1 e 5, vai mostrar
       print('Opção inválida. Tente novamente.') # esta mensagem de opção invalida
print('Finalizando...') # vai finalizar o programa quando o usuario apertar o 5
print('--=' * 10)
sleep(2) # vai esperar por 2 segundo
print('Fim do programa! Volte sempre! ') # e vai dar fim ao programa e um adeus