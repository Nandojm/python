lanche = 'Hamburguer','Suco','Pizza', 'Pudim', 'Batata Frita'
css = ('\033[35m--\033[m' * 20)
for comida in range (0, len(lanche)):
    print(f'Meu lanche foi {lanche[comida]}')
print(css)
for comida in lanche:
    print(f'Meu lanche foi {comida}')
print(css)
for pos, comida in enumerate (lanche):
    print(f'Meu lanche foi {comida} na posição {pos}')
print('Comi muito hoje.')
print(css)
print(sorted(lanche))
a = (2,5,4)
b = (5,8,1,2)
c = a+b
print(c)