from random import randint
n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)
numeros = (n1,n2,n3,n4,n5)
print(f'Os números sorteados foram: ',end=' ')
for nu in numeros:
    print(nu, end=' ')
maior = max(numeros)
menor = min(numeros)
print(f'\nO maior número foi {maior}')
print(f'E o menor número foi {menor}')


