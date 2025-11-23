lista = ('arroz','cachorro','carro','Borboleta','celular',
            'bicicleta', 'papagaio', 'estrela', 'lua', 'computador',
            'caixa','jumento', 'aviao')
for palavra in lista: # aqui checa cada palavra da lista.
    print(f'\nNa palavra {palavra.upper()} tem as vogais:',end=' ')
    for v in palavra: # já aqui o V vai checar cada letra da palavra na lista.
        if v in 'aeiou': # se a letra da palavra for igual a AEIOU
            print(v, end=' ') # print as vogais