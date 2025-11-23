media = 0
soma = 0
nome_homen = 0
homen_velho = 0
mulher_menor = 0
for c in range(1,4):
    print('---- {}º PESSOA -----'.format(c))
    nome = str(input('Qual é o seu nome ?'))
    idade = int(input('Qual é a sua idade ?'))
    print('[1] Masculino '
          '[2] Feminino')
    sexo = int(input('Qual é o seu sexo ? '))
    soma += idade
    if c == 1 and idade == 1:
        nome_homen = nome
        homen_velho = idade
    if sexo == 1 and idade > homen_velho:
        nome_homen = nome
        homen_velho = idade
    elif sexo == 2 and idade < 18:
        mulher_menor +=1
media = soma / 3
print('A média de idade das pessoas é de {:.1f} anos'.format(media))
print('A idade do homen mais velho é {} anos e ele se chama {} .'.format(homen_velho,nome_homen))
print('Temos {} mulheres menos de 18 anos'.format(mulher_menor))