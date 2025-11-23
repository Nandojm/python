import random
p2 = input('Digite o nome do Professor: ')
print ('Ola professora {}! Seja bem vinda!' . format((p2)))
a1 = input('Agora gostaria que me fala-se o nome do primeiro aluno: ')
a2 = input( 'Agora o do segundo aluno: ')
a3 = input('E para finalizar me diga o terceiro aluno: ')
nome = [a1, a2, a3]
print ('Muito obrigado professora {}, agora que ja sabemos que os participante são {}, {} e {} vamos começar o sorteio.'
       ''.format(p2, nome[0], nome[1], nome[2]))
random.shuffle(nome)
print('A ordem vai ser, em primeiro lugar {}. \nEm segundo lugar {}.\nE para finalizar {}.'.format(nome[0], nome[1], nome[2]))

