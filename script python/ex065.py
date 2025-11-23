contador = maior = menor = soma = 0
while True:
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1
    if contador == 1:
        maior = numero
        menor = numero
        primeiro = False
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    while True:
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()
        if cont in ('S','N'):
            break
        print('Tente novamente.')
    if cont == 'N':
        break
media = soma / contador
print(f'Você digitou {contador} números e a média foi {media:.2f}')
print(f'O maior numero foi {maior} e menor foi {menor}')