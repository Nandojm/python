from random import choice
print(' ')


jogador = str(input('Qual você escolhe ? ')).strip().lower() # aqui o jogador escolhe (pedra, papel ou tesoura)
jogo = ["pedra", "tesoura", "papel"] # aqui coloquei as opçoes em uma lista separadas por VIRGULAS.
computador = choice(jogo) # Aqui mandei escolher na lista acima uma opção (pedra, papel ou tesoura.

if computador == 'pedra' and jogador == 'pedra': # se o computador escolhe pedra igual ao jogador venci.
    print('PARABÉNS! Você é mesmo bom nisso, você me ganho.')
elif computador == 'tesoura' and jogador == 'tesoura': #agora de computador escolher tesoura  igual ao jogador eu venci.
    print('PARABÉNS! Você é mesmo bom nisso, você me ganho.')
elif computador == 'papel' and jogador == 'papel': # agora se o computador escolher papel igual ao jogador eu também venci.
    print('PARABÉNS! Você me ganhou, você é muito bom.')
else: #agora se não for igual a nenhum outro de cima, o computador venceu.
    print('Você errou eu eu pensei em {}'.format(computador))