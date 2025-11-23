numeros = (int(input('Digite um número: ')),int(input('Digite um outro número: ')),
           int(input('Digite mais um número: ')),int(input('Digite o ultimo número: ')),)
print(f'Você digitou os valores {numeros}')
contador = 0
for nu in numeros:
    if nu == 9:
        contador +=1
print(f'O valor 9 apareceu {contador} vezes')
for pos, nu in enumerate(numeros):
    if nu == 3:
        print(f'O numero 3 apareceu na {pos+ 1} posição')
        break
else:
    print('O numero 3 não aparece nenhuma vez')

print(f'Os valores pares digitados foram: ', end='')
for nu in numeros:
    if nu % 2 == 0 :
        print(nu, end=' ')

