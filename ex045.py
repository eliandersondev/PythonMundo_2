'''
Desafio 045

Crie um programa que faça o computador jogar
Jokempô com você.
'''
from random import randint
from time import sleep
print('{:=^40}'.format(' JOKEMPÔ '))
print('Vamos Jogar!!!')
print('[1] PEDRA - [2] PAPEL - [3] TESOURA')

item = ['JOGO','PEDRA','PAPEL','TESOURA']
jogador = int(input('Qual é a sua jogada? '))
computador = randint(1,3)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')

print('-=' * 15)
print('Jogador jogou {}'.format(item[jogador]))
print('Computador jogou {}'.format(item[computador]))
print('-=' * 15)

if jogador == computador:
    print('EMPATE')
elif jogador == 1 and computador == 3:
    print('Jogador VENCEU.')
elif jogador == 1 and computador == 2:
    print('Computador VENCEU.')
elif jogador == 2 and computador == 1:
    print('Jogador VENCEU.')
elif jogador == 2 and computador == 3:
    print('Computador VENCEU.')
elif jogador == 3 and computador == 1:
    print('Computador VENCEU.')
elif jogador == 3 and computador == 2:
    print('Jogador VENCEU.')
else:
    print('JOGADA INVÁLIDA')
