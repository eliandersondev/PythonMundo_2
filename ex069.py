'''
Desafio 069

Crie um programa que leia a idade e o sexo de
várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continur.
No final, mostre:

A - quantas pessoas tem mais de 18 anos.
B - quantos homens foram cadastrados.
C - Quantas mulheres tem menos de 20 anos.

'''

homem = mulher = total = 0
while True:
    print('-' * 40)
    print('{:^40}'.format('CADASTRE UMA PESSOA'))
    print('-' * 40)
    idade = int(input('Idade: '))
    sexo = 'x'
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F] ')).strip().upper()
    print('-' * 40)

    if idade > 18:
        total += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1

    continuar = 'x'
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()

    if continuar == 'N':
        break

print('Total de pessoas com mais de 18 anos: {}.'.format(total))
print('Ao todo temos {} homens cadastrados.'.format(homem))
print('E temos {} mulheres com menos de 20 anos.'.format(mulher))
