'''
Desafio 071

Crie um programa que simule o funcionamento de um caixa
eletrônico. No início, pergunte ao usuário qual será o
valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de
R$ 50, R$ 20, R$ 10 e R$ 1
'''

print('=' * 45)
print('{:^60}'.format('BANCO CEV'))
print('=' * 45)

valor = int(input('Que valor você quer sacar? R$ '))

tot50 = tot20 = tot10 = tot1 = 0
montante = valor

if int(montante / 50) > 0:
    tot50 = int(montante / 50)
    montante = montante - (tot50 * 50)
    print('Total de {} cédulas de R$ 50'.format(tot50))
if int(montante / 20) > 0:
    tot20 = int(montante / 20)
    montante = montante - (tot20 * 20)
    print('Total de {} cédulas de R$ 20'.format(tot20))
if int(montante / 10) > 0:
    tot10 = int(montante / 10)
    montante = montante - (tot10 * 10)
    print('Total de {} cédulas de R$ 10'.format(tot10))
if 0 < montante < 10:
    tot1 = montante
    montante = montante - tot1
    print('Total de {} cédulas de R$ 1'.format(tot1))






print('=' * 45)
print('Volte sempre ao BANCO DEV! Tenha um bom dia!')