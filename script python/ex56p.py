soma_idade = 0
media_idade = 0
maior_idade_homen = 0
nome_velho = ''
total_mulher_20 = 0
for p in range (1,4):
    print('----- {}º PESSOA -----'.format(p))
    nome = str(input('Nome: '.format(p))).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':  # aqui descobri a primeira pessoa
        maior_idade_homen = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homen: # aqui faço o teste nas outras pessoa e se for o que eu quero ele substitui o anterior
        maior_idade_homen = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1
media_idade = soma_idade / 3
print('A média de idade do grupo é de {:.1f} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homen, nome_velho))
print('Ao total são {} mulheres com menos de 20 anos'.format(total_mulher_20))