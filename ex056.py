'''
Desafio 056

Desenvolva um programa que leia o nome, idade, sexo de 4 pessoas.
No final do programa mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
'''

soma = idade_homem = quant_mulher = 0

for c in range(1, 5):
    print('----- {}a PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))

    sexo = 'x'
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()

    soma += idade

    if sexo == 'M'and idade > idade_homem:
        idade_homem = idade
        nome_homem = nome

    if sexo == 'F'and idade < 20:
        quant_mulher += 1


media = soma / 4

print('A média de idade do grupo é de {:.2f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(idade_homem, nome_homem))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(quant_mulher))


