from random import randint
nu1 = randint(0,10)
nu2 = randint(0,10)
nu3 = randint(0,10)
nu4 = randint(0,10)
nu5 = randint(0,10)
numeros = (nu1,nu2,nu3,nu4,nu5)
print(f'O valores sorteados foram: ',end='')
for n in numeros:
    print(n, end=' ')

menor = numeros[0]
for nu in numeros:
    if nu < menor:
        menor = nu
print(f'\nO menor numero foi {menor}')

maior = numeros[0]
for nu in numeros:
    if nu > maior:
        maior = nu
print(f'\nO maior numero foi {maior} ')

