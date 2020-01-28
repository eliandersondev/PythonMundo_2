'''
Desafio 039
Façaum programa que leia o ano de nascimento de um jovem
e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo de alistamento.

Seu programa também deverá mostrar o tempo que falta ou
que passou do prazo.
'''
from datetime import date


ano_atual = date.today().year
print('ALISTAMENTO MILITAR')
ano = int(input('Informe o seu ano de nascimento: '))
idade = ano_atual - ano
if idade < 18:
    print('Faltam {} anos para o alistamento.'.format(18-idade))
elif idade ==18:
    print('Corra para fazer o seu alistamento, \nesse é o seu ano!')
else:
    print('Se você não fez o alistamento, \ndirija-se até órgão responsável. Já se passou {} anos.'.format(((idade-18))))