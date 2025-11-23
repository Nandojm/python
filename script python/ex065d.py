continuar = 'S'
contador = menor = maior = soma = 0
while continuar in 'Ss':
    nu = int(input('Digite um numero: '))
    contador += 1
    soma += nu
    if contador == 1:
        maior = menor = nu
    else:
        if nu > maior:
            maior = nu
        if nu < menor:
            menor = nu
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / contador
print(f'Você digitou {contador} números e a média foi {media:.2f}')
print(f'O maior número é {maior} e o menor foi {menor}')