from random import randint
numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),
           randint(0,10),randint(0,10))
print('Os números gerados foram: ',end='')
for c in numeros:
    print(c, end=' ')
maior = numeros[0]
for nu in numeros:
    if nu > maior:
        maior = nu
print(f'\nO maior número foi {maior}')
menor = numeros[0]
for c in numeros:
    if c < menor:
        menor = c
print(f'\nE o menor número foi {menor}')