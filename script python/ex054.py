import datetime
data = datetime.date.today().year
menor = 0
maior = 0 # aqui serve para iniciar a contagem
idade = 0  # quando tiver que usar uma variavel dentro do FOR tenho que inicia ela fora com o valor 0
for c in range(1,8):
    ano_nasc = int(input('Em que ano a {}º pessoa nasceu'.format(c)))
    idade =  data - ano_nasc
    if idade >= 21 :
       maior += 1 #Incrementa o contador se a idade for maior ou igual a 21
    else:
        menor +=1
print('São {} pessoas menores de idade'.format(menor))
print('São {} pessoas maiores de idade'.format(maior))# mostra a quantidade