from time import sleep
inicio = True
contador = 0
soma = maior = menor = 0
while True:
    try:
        numero = int(input('Digite um numero: '))
    except ValueError:
        print ('[\033[31mERRO\033[m] Digite apenas numeros.')
        print('')
        continue
    contador += 1
    soma += numero
    if inicio:
        maior = numero
        menor = numero
        inicio = False
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
        if continuar in ('N','S'):
            break
        print('--' * 15)
        sleep(1)
        print('[\033[31mERRO\033[m] Tente novamente.')
        print('--' * 15)
        sleep(1)
    if continuar == 'N':
        break
media = soma / contador
print(f'Você digitou {contador} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
