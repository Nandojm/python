#print('\033[0;33;44mOla, Mundo\033[m')
"""a = 3
b = 5
print('Os valores são \033[33m{}\033[m e \033[32m{}\033[m !'.format(a, b))"""
nome = 'Nando'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m'}
print('Ola! Muito prazer em te connhecer, {}{}{}!!!'.format(cores ['azul'], nome, cores[ 'limpa']))