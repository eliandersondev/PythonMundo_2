'''
Desafio 054

Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas jão são maiores.
'''

from datetime import date

ano = date.today().year
maiores = 0
menores = 0

for c in range(7):
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = ano - nascimento
    if idade < 21:
        menores += 1
    else:
        maiores += 1
print('-=' * 20)
print('O número de pessoas maiores de 21 anos é {}'.format(maiores))
print('O número de pessoas menores de 21 anos é {}'.format(menores))
