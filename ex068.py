'''
Desafio 068
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.

'''
from random import randint
print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 30)

soma = cont = 0
while True:
    num = int(input('DIGA UM VALOR: '))
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = str(input('PAR OU ÍMPAR? [P/I] ')).strip().upper()

    print('-' * 60)
    computador = randint(1, 5)
    soma = num + computador

    if (soma % 2) == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print('Você jogou {} e o computador {}. Total de {} DEU {}'.format(num, computador, soma, resultado))

    if resultado[0] == escolha:
        cont += 1
    elif resultado[0] == escolha:
        cont += 1
    else:
        print('Você PERDEU!')
        break

    print('-' * 60)
    print('Você VENCEU!')
    print('Vamos jogar novamente...')
    print('=-' * 30)

print('=-' * 30)
print('GAME OVER! Você venceu {} vezes.'.format(cont))