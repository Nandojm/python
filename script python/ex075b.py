numeros = (int(input('Digite um número: ')),int(input('Digite um outro número: ')),
           int(input('Digite mais um número: ')),int(input('Digite o ultimo número: ')),)
print(f'Os números digitados foram {numeros}')
print(f'O número 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 aparece na {numeros.index(3) + 1}ª posição')
else:
    print(f'O número 3 não aparece em nenhuma posição.')
print('Os números pares foram ',end='')
for nu in numeros:
    if nu % 2 == 0:
        print(nu, end=' ')