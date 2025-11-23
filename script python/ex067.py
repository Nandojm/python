mult = num = contador = 0
while  True: # este while vai iniciar o loop infinito
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('--' * 15)
    if num < 0: # o loop so vai se incerrado se o usuario digitar um numero NEGATIVO
        break
    for c in range (1, 11):# Dentro no while este for vai se repetir nos 10 primeiros numeros
        print(f'{num} x {c} = {num*c} ') # e mostrar os 10 resultado da tabuada. Observação: posso fazer a soma direto na formatação do print
    print('--' * 15)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')