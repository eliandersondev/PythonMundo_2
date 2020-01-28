'''Desafio 058

Melhore o jogo do Desafio 028 onde o computador vai
'pensar' em um número entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários
para vencer.
'''
from random import randint
print('JOGO DA ADVINHAÇÃO')
computador = randint(0, 10)
cont = 1
jogador = int(input('Tente advinhar o número que eu estou pensando entre 0 e 10: '))
while jogador != computador:
    jogador = int(input('Tente novamente: '))
    cont += 1
print('Meus Parabéns, você acertou na {} vez.'.format(cont))

