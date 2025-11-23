from random import randint
numeros = tuple(randint(0,10) for c in range(5))
print('O números gerados foram: ', end='')
for nu in numeros:
    print(nu, end=' ')
print(f'\nO maior número foi {max(numeros)}')
print(f'E o menor número foi {min(numeros)}')