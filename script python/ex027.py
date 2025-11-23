nome =  str(input('Digite seu nome completo: ')).strip()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(nome.split() [0] ))# peguei o nome e coloquei cada parte em bloco e mostrei que queria o primeiro [0]
print('Seu ultimo nome é {}.'.format(nome.split() [-1] ))# o [-1] se refere ao último objeto de uma lista, começando do último para o primeiro sem identifica a quantidade.

no = str(input('Digite seu nome Completo: ')).strip()
nome = no.split()
print('Seu primeiro nome é {}.'.format(nome [0] ))
print('Seu segundo nome é {}.'.format(nome[ len(nome)-1] )) # quando se usa o len, você já utiliza uma lista quantificada, sendo assim, você ordena uma lista de forma numerica.