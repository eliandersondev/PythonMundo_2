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

cedula = 50
montante = valor
cont = 0

while True:
    if montante >= cedula:
        montante -= cedula
        cont += 1
    else:
        if cont > 0:
            print('Total de {} cédulas de R$ {}'.format(cont, cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cont = 0
        if montante == 0:
            break


print('=' * 45)
print('Volte sempre ao BANCO DEV! Tenha um bom dia!')