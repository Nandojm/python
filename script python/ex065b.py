from time import sleep
contador = 1
maior = menor = 0
soma = 0
primeiro = True
while True:
    numero = int(input('Digite um número: '))
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    print('--' * 15)
    if cont != 'N' and cont != 'S':# este if vai verificar se cont vai ser diferente de S e N, se for
        sleep(1)
        print('Resposta invalida') # vai mostrar este erro e vai repetir a pergunta
        print('--' * 15)
        sleep(1)

    else:# se nao for, vai rodar o programa.
        if primeiro: # este if vai fazer maior e menor receber os numeros.
            maior = numero
            menor = numero
            primeiro = False # vai transforma primeiro em falso, assim faz a verificação e acaba.
        else: # em seguida
            if numero > maior: # aqui vai verificar se numero é maior que maior
                maior = numero # se for, maior vai ser atualizado para o maior
            if numero < menor: # o mesmo vai ser feito aqui com o menor
                menor = numero
        if  cont == 'S': # se o usuario quiser continuar
            contador += 1 # vai contar mais um
            soma += numero
        elif cont == 'N': # Aqui vai ser nao
            soma += numero # soma o ultimo numero
            break # e fecha o programa
print(f'Você digitou {contador} e a osma foi {soma}')
print(f'O maior foi {maior} e o menor número foi {menor}')



