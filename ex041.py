'''
Desafio 041

A confederação nacional de natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:

- até 9 anos: Mirim
- até 14 anos: Infantil
- até 19 anos: Junior
- até 20 anos: Sênior
- Acima: Master
'''


from datetime import datetime

ano_atual = datetime.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano

if idade <= 9:
    print('A sua categoria é Mirim.')
elif idade <= 14:
    print('A sua categoria é Infantil.')
elif idade <= 19:
    print('A sua categoria é Junior.')
elif idade <= 25:
    print('A sua categoria é Sênior.')
else:
    print('A sua categoria é Master.')