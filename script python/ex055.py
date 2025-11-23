peso_min = 0 # aqui criei a variavel peso_min com valor 0 para
peso_max = 0 # aqui fiz o mesmo para peso_max
for c in range (1,6):  # formei um loop para recolher 5 pesos de pessoa
    peso  = float(input('Peso da {}º pessoa: '.format(c))) # recebi os pesos das 5 pessoas com o loop
    if c == 1: # aqui fez o loop rodar a primeira vez para poder recolher os pesos de todos e
        peso_max = peso # salvar o mais pesado em peso_max
        peso_min = peso # e o menor peso em peso_min

    else:
        if peso > peso_max: # aquir testei se peso for maior que o peso_max
            peso_max = peso # peso_max vai deixar de ser zero e vai receber o maior peso
        if peso < peso_min: # aqui aconteceu se peso for menor que peso_min
            peso_min = peso #peso_min vai deixar de ser zero e vai passar a receber o menor peso.

print('O maior peso lido foi de {}Kg'.format( peso_max))
print('O menor peso lido foi de {}Kg'.format(peso_min))
